## Enrich Data

In this module, you'll see how you can enrich incoming streaming data with pre-stored metadata. In this case, the device data is enriched with information such as who manufactured the device, based on device ID. 

### What was created

The CloudFormation template that you ran during Set Up deployed the following:

* A **Kinesis Firehose** ingesting de-identified data.
* A **Enrich** Lambda function that looks up the metadata in Dynamo, and writes the enriched message back into the Kinesis Firehose.
* A **DeviceDetails** DynamoDB table with metadata.
* An **S3 bucket** to store the enriched data from Kinesis.

### Ingest Data
In order to allow these modules to be completed out of order, we have provided two options for proceeding:

#### I've completed Module 1
If you have already completed Module 1, data is already streaming in from the simulated data you published earlier.

1. TODO

#### I haven't completed Module 1
If you haven't completed the first module, you will use **Kinesis Data Generator** to simulate incoming data coming into the **IngestStream** Kinesis Firehose.

1. Go to the [Kinesis Data Generator Set Up page][kdg-help].

1. Follow the instructions. Once you're done, log into [KDG][kdg] with the credentials you just created.

1. Select **us-west-2** from the **Region** dropdown.

1. Confirm that **IngestStream** is selected in the **Stream/delivery stream** dropdown.

1. Under **Record template**, copy paste the following into the template box:

	```
	{
		"timestamp": "{{date.now}}",
		"device_id": "device{{helpers.replaceSymbolWithNumber("####")}}",
		"patient_id": "patient{{helpers.replaceSymbolWithNumber("####")}}",
		"name": "{{name.lastName}}, {{name.firstName}}",
		"dob": "{{random.number(12)}}/{{random.number(30)}}/{{random.number({"min":1920,"max":2000})}}",
		"temp": {{random.number({"min":96,"max":104})}},
		"pulse": {{random.number({"min":50,"max":120})}},
		"oxygen_percent": {{random.number({"min":80,"max":100})}},
		"systolic": {{random.number({"min":80,"max":200})}},
		"diastolic": {{random.number({"min":40,"max":120})}}
	}
	```

1. Click **Send data**. KDG is now sending simulated data to your Kinesis Firehose.

### Monitor the Pipeline
To allow you to more easily monitor this section of the pipeline, we created a CloudWatch dashboard that displays Lambda invocations, Kinesis Firehose records, and DynamoDB table reads.

1. Go to the **CloudWatch** console, go to **Dashboards**, and click on the **StreamingITL** dashboard. 

1. After a few minutes, you'll see points starting to show up in the dashboard. 

1. You can also confirm that the pipeline is working by checking S3 for transformed records.

1. Go to the **S3** console and TODO enriched/ de-identified/

### Summary
TODO

### Next

:white_check_mark: Continue to the second module: [Detect Anomalies][detect-anomalies].

[kdg-help]: https://awslabs.github.io/amazon-kinesis-data-generator/web/help.html
[kdg]: https://awslabs.github.io/amazon-kinesis-data-generator/web/producer.html
[detect-anomalies]: ../3_DetectAnomalies/