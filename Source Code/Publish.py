import json
import boto3
import os
from random import randint, uniform
from datetime import datetime
  
print('Loading function')
  
def lambda_handler(event, context):
	iot = boto3.client('iot-data')

	# publish 10 messages at a time
	for i in range(10):
		# simulate random data
		data = {
			'timestamp': datetime.now().strftime('%Y-%m-%dT%H:%M:%S'),
			'device_id': 'device' + str(randint(1000,10000)),
			'patient_id': 'patient' + str(randint(1000,10000)),
			'name': ''.join(random.choice(string.lowercase) for x in range(20)).join(', ').''.join(random.choice(string.lowercase) for x in range(10)),
			'dob': str(randint(1,13)) + '/' + str(randint(1,30)) + '/' + str(randint(1920,2000)),
			'temp': round(uniform(96,104),1),
			'pulse': round(uniform(50,120),1),
			'oxygen_percent': round(uniform(80,100),1),
			'systolic': round(uniform(80,200),1),
			'diastolic': round(uniform(40,120),1)
		}
		
		text = json.dumps(data)
		print(text)

		# publish to topic
		response = iot.publish(
		    topic=os.environ['IoTTopic'],
		    qos=0,
		    payload=text.encode()
		)
		
		print('IoT Publish: ',json.dumps(response))