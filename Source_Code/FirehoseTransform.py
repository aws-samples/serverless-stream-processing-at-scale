import base64
import json
import boto3
from datetime import datetime
import time
import os
import random

print('Loading function')

# DDB Table name
TABLE_NAME = os.environ['TABLE_NAME']

# DDB Batch Size Max
DDB_BATCH_SIZE = 100

# cache timeout in seconds
CACHE_TIMEOUT = 15*60 # 15 minutes

# default encoding of bytes in the posted record
ENCODING = 'utf-8'

class Cache:
    def __init__(self, age):
        self.age = age
        self.store = {}

    def get(self, key):
        if key in self.store:
            v = self.store[key]
            exp = v['expiry']
            now = time.time()
            if(now < exp):
                return v['data']
            else:
                self.store.pop(key)
        return None

    def put(self, key, data):
        exp = time.time() + self.age
        self.store[key] = {
          'expiry' : exp,
          'data' : data
        }

class Database:
    def __init__(self, ddb):
        self.ddb = ddb
        self.cache = Cache(CACHE_TIMEOUT)


    def queryDDB(self, device_id_list, response):
        attempt = 0
        # loop with delay until MAX_ATTEMPTS or we have no more unprocessed records
        while(attempt < MAX_ATTEMPTS):
            unprocessed = []
            self.batchQueryDDB(device_id_list, response, unprocessed)
            if(len(unprocessed) == 0):
                break
            else:
                delay = expBackoffFullJitter(attempt)
                time.sleep(delay)
                attempt += 1
                device_id_list = unprocessed

    def batchQueryDDB(self, device_id_list, response, unprocessed):
        print("Querying details for {} devices from DynamoDB".format(len(device_id_list)))

        for i in range(0, len(device_id_list), DDB_BATCH_SIZE):
            keys = []
            j = i
            while j < len(device_id_list) and j < (i + DDB_BATCH_SIZE):
                device_id = device_id_list[j]
                j += 1
                keys.append({
                    'device_id' : device_id
                })


            result = self.ddb.batch_get_item(
                RequestItems = {
                    TABLE_NAME : {
                        'Keys' : keys
                    }
                }
            )

            for r in result['Responses'][TABLE_NAME]:
                device_id = r['device_id']

                device_details = {
                    'manufacturer' : r['manufacturer'],
                    'model' : r['model']
                }

                self.cache.put(device_id, device_details)
                response[device_id] = device_details

            unproc_count = 0
            if TABLE_NAME in result['UnprocessedKeys']:
                unproc = result['UnprocessedKeys'][TABLE_NAME]["Keys"]
                unproc_count = len(unproc)
                for u in unproc:
                    unprocessed.append(u['device_id'])

            print("DDB Query: {} results, {} unprocessed out of {} keys".format(
                len(result['Responses'][TABLE_NAME]),
                unproc_count,
                len(keys)))

    def getDeviceDetails(self, device_id_set):
        response = {}
        query_device_ids = []

        for device_id in device_id_set:
            device_details = self.cache.get(device_id)
            if(device_details is None):
                query_device_ids.append(device_id)
            else:
                response[device_id] = device_details

        if len(query_device_ids) > 0:
            self.queryDDB(query_device_ids, response)
        return response

# Exponential Backoff Retry with "Full Jitter" from:
# https://aws.amazon.com/blogs/architecture/exponential-backoff-and-jitter/
BASE = 2 # seconds
CAP = 10 # seconds
MAX_ATTEMPTS = 5 # retry 5 times max

def expBackoffFullJitter(attempt):
    return random.uniform(0, min(CAP, pow(2, attempt)*BASE))

ddb = boto3.resource('dynamodb')
database = Database(ddb)

def lambda_handler(event, context):
    source_records = []
    query_devices = set()

    print("Received batch of {} records".format(len(event['records'])))

    for record in event['records']:
        payload = base64.b64decode(record['data']).decode(ENCODING)

        event = json.loads(payload)

        source_records.append({
            'recordId' : record['recordId'],
            'event' : dict(event) # copy of event
        })

        query_devices.add(event['device_id'])

    device_details = database.getDeviceDetails(query_devices)

    output = []
    successes = 0

    for record in source_records:
        event = record['event']
        device_id = event['device_id']

        if(device_id in device_details):
            # we have device details
            details = device_details[device_id]

            # copy existing event
            trans_event = dict(event)

            # enrich event with device details
            trans_event['manufacturer'] = details['manufacturer']
            trans_event['model'] = details['model']

            trans_payload = json.dumps(trans_event) + "\n"

            output_record = {
                'recordId': record['recordId'],
                'result': 'Ok',
                'data': base64.b64encode(trans_payload.encode(ENCODING)).decode(ENCODING)
            }
            successes += 1
            output.append(output_record)
        else:
            # we couldn't get device details: flag that as an error to firehose
            print("ProcessingFailed: couldn't find device " + str(device_id))
            output_record = {
                'recordId': record['recordId'],
                'result': 'ProcessingFailed',
                'data': None
            }
            output.append(output_record)

    print('Successfully processed {} out of {} records.'.format(successes, len(source_records)))
    return {'records': output}
