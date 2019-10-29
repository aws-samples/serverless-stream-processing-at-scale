import json
import boto3
import os
from decimal import Decimal
  
print('Loading function')
  
def lambda_handler(event, context):
    # print IoT message
    iot_msg = json.dumps(event)
    print('Received event: ',iot_msg)

    # put PHI/PII into dynamo
    dynamodb = boto3.resource('dynamodb', region_name='us-west-2')
    table = dynamodb.Table(os.environ['TableName'])

    response = table.put_item(
        Item={
            'PatientID': event["PatientID"],
            'Timestamp': event["Timestamp"],
            'device_id': event["device_id"],
            'Name': event["Name"],
            'dob': event["dob"],
            'Temp': Decimal(str(event["Temp"])),
            'OxygenPercent': Decimal(str(event["OxygenPercent"]))
        }
    )

    print('Dynamo PutItem: ',json.dumps(response))

    # de-identify data
    event["device_id"] = None
    event["Name"] = ''
    event["dob"] = ''
    event["Temp"] = None
    event["OxygenPercent"] = None

    de_identified = json.dumps(event)
    print('De-Identified: ',de_identified)

    # put de-identified data into kinesis
    firehose = boto3.client('firehose')
    response = firehose.put_record(
    DeliveryStreamName=os.environ['DeliveryStream'],
        Record={
            'Data': de_identified.encode()
        }
    )

    print('Kinesis Firehose PutRecord: ',json.dumps(response))
