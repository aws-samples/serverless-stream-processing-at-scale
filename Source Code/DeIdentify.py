import json
import boto3
import os
from decimal import Decimal
  
print('Loading function')

dynamodb = boto3.resource('dynamodb', region_name='us-west-2')
table = dynamodb.Table(os.environ['TableName'])
firehose = boto3.client('firehose')
  
def lambda_handler(event, context):
    # print IoT message
    iot_msg = json.dumps(event)
    print('Received event: ',iot_msg)

    # put PHI/PII into dynamo
    response = table.put_item(
        Item={
            'patient_id': event["patient_id"],
            'timestamp': event["timestamp"],
            'device_id': event["device_id"],
            'name': event["name"],
            'dob': event["dob"],
            'temp': Decimal(str(event["temp"])),
            'oxygen_percent': Decimal(str(event["oxygen_percent"]))
        }
    )

    print('Dynamo PutItem: ',json.dumps(response))

    # de-identify data
    event["name"] = ''
    event["dob"] = ''
    event["temp"] = None
    event["oxygen_percent"] = None

    de_identified = json.dumps(event)
    print('De-Identified: ',de_identified)

    # put de-identified data into kinesis
    response = firehose.put_record(
    DeliveryStreamName=os.environ['DeliveryStream'],
        Record={
            'Data': de_identified.encode()
        }
    )

    print('Kinesis Firehose PutRecord: ',json.dumps(response))
