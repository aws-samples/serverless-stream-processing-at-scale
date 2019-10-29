import json
import boto3
import os
from random import randint, uniform
from datetime import datetime
  
print('Loading function')
  
def lambda_handler(event, context):
	# create random fake data
	data = {
		'Timestamp': datetime.now().strftime('%Y-%m-%dT%H:%M:%S'),
		'device_id': 'device' + str(randint(1000,10000)),
		'PatientID': 'patient' + str(randint(1000,10000)),
		'Name': 'lastname firstname',
		'dob': str(randint(1,13)) + '/' + str(randint(1,30)) + '/' + str(randint(1920,2017)),
		'Temp': round(uniform(96,105),1),
		'pulse': round(uniform(40,120),1),
		'OxygenPercent': round(uniform(80,100),1),
		'systolic': round(uniform(80,200),1),
		'diastolic': round(uniform(40,100),1)
	}
	
	text = json.dumps(data)
	print(text)

	# publish data
	iot = boto3.client('iot-data')
	response = iot.publish(
	    topic=os.environ['IoTTopic'],
	    qos=0,
	    payload=text.encode()
	)
	
	print('IoT Publish: ',json.dumps(response))