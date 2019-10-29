import boto3
import json
import requests
import os
import random
from botocore.vendored import requests
import json
 
print('Loading function')

SUCCESS = "SUCCESS"
FAILED = "FAILED"

DEVICES = 10000
MANUFACTURERS = 20
MODELS = 20

ddb = boto3.resource('dynamodb')
table = ddb.Table(os.environ['TABLE_NAME'])

def lambda_handler(event, context):
    print(event)
    reqtype = event['RequestType']

    if (reqtype == 'Create'):
        populate()

    # send cfn response to tell the cfn stack that this was successful
    send(event,context,SUCCESS,{})

def populate():
    for i in range(0, DEVICES):
        item = {
                'device_id' : 'device{num:04d}'.format(num=i),
                'manufacturer' : 'Manufacturer {num:02d}'.format(num = random.randrange(MANUFACTURERS)),
                'model' : 'Model {num:02d}'.format(num = random.randrange(MODELS))
                }

        if(i % 100 == 0):
            print('Adding ' + json.dumps(item))
        table.put_item(Item = item)
 
# cfn response
def send(event, context, responseStatus, responseData, physicalResourceId=None, noEcho=False):
    responseUrl = event['ResponseURL']
 
    print(responseUrl)
 
    responseBody = {}
    responseBody['Status'] = responseStatus
    responseBody['Reason'] = 'See the details in CloudWatch Log Stream: ' + context.log_stream_name
    responseBody['PhysicalResourceId'] = physicalResourceId or context.log_stream_name
    responseBody['StackId'] = event['StackId']
    responseBody['RequestId'] = event['RequestId']
    responseBody['LogicalResourceId'] = event['LogicalResourceId']
    responseBody['NoEcho'] = noEcho
    responseBody['Data'] = responseData
 
    json_responseBody = json.dumps(responseBody)
 
    print("Response body:\n" + json_responseBody)
 
    headers = {
        'content-type' : '',
        'content-length' : str(len(json_responseBody))
    }
 
    try:
        response = requests.put(responseUrl,
                                data=json_responseBody,
                                headers=headers)
        print("Status code: " + response.reason)
    except Exception as e:
        print("send(..) failed executing requests.put(..): " + str(e))
