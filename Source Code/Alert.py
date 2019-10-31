import boto3
import base64
import os
import json
from base64 import b64decode, b64encode

print('Loading function')

sns = boto3.client('sns')
topic_arn = os.environ['SNS_TOPIC_ARN']
upper_threshold = float(os.environ['UPPER_THRESHOLD'])
lower_threshold = float(os.environ['LOWER_THRESHOLD'])

ENCODING = 'utf-8'
def lambda_handler(event, context):
    output_records = []
    
    for record in event['records']:
        data = b64decode(record['data']).decode(ENCODING)
        data_json = json.loads(data)
        print("Data: ",json.dumps(data_json))
        anomaly_score = data_json['ANOMALY_SCORE']

        anomaly_found = False
        
        if anomaly_score > upper_threshold:
            anomaly_found = True
            response = sns.publish(TopicArn=topic_arn, Message=data, Subject='Anomaly Score Above ' + str(upper_threshold))
            print('SNS Publish: ',json.dumps(response))
        elif anomaly_score < lower_threshold:
            anomaly_found = True
            response = sns.publish(TopicArn=topic_arn, Message=data, Subject='Anomaly Score Below ' + str(lower_threshold))
            print('SNS Publish: ',json.dumps(response))

        data_json['anomaly'] = anomaly_found

        add_newline = json.dumps(data_json) + "\n"
        output = b64encode(add_newline.encode(ENCODING)).decode(ENCODING)

        output_records.append({
            'recordId': record['recordId'],
            'result': 'Ok',
            'data': output
        })

    return {'records': output_records}
