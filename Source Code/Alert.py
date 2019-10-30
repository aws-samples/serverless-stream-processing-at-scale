import boto3
import base64

print('Loading function')

client = boto3.client('sns')
topic_arn = os.environ['SNS_TOPIC_ARN']
threshold = os.environ['ANOMALY_THRESHOLD']

def lambda_handler(event, context):
    for record in event['records']:
        data = record['data']
        if data["ANOMALY_SCORE"] > threshold:
            response = sns.publish(TopicArn=topic_arn, Message=base64.b64decode(data), Subject='Anomaly Score Above ' + str(threshold))
            print('SNS Publish: ',json.dumps(response))
