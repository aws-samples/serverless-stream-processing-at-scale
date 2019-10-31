import json
import string
import boto3
import os
from random import randint, uniform, choice
from datetime import datetime
  
print('Loading function')

iot = boto3.client('iot-data')
  
def lambda_handler(event, context):
	# publish multiple messages at a time
	for i in range(2000):
		# simulate random data
		lastname = choice(string.ascii_uppercase) + ''.join(choice(string.ascii_lowercase) for i in range(randint(5,15)))
		firstname = choice(string.ascii_uppercase) + ''.join(choice(string.ascii_lowercase) for i in range(randint(4,8)))
		data = {
			'timestamp': datetime.now().strftime('%Y-%m-%dT%H:%M:%S'),
			'device_id': 'device' + str(randint(0,4500)).zfill(4),
			'patient_id': 'patient' + str(randint(0,5000)).zfill(4),
			'name': lastname + ', ' + firstname,
			'dob': str(randint(1,13)) + '/' + str(randint(1,30)) + '/' + str(randint(1920,2000)),
			'temp': round(uniform(96,104),1),
			'pulse': round(uniform(0,60),1) if (i%500 == 0) else round(uniform(60,120),1), # create an anomaly
			'oxygen_percent': round(uniform(80,100),1),
			'systolic': round(uniform(80,200),1),
			'diastolic': round(uniform(40,120),1)
		}
		
		text = json.dumps(data)
		print(text)

		# publish to topic
		response = iot.publish(
		    topic=os.environ['IoTTopic'] + 'Hospital' + str(randint(0,50)).zfill(2) + '/',
		    qos=0,
		    payload=text.encode()
		)
		
		print('IoT Publish: ',json.dumps(response))