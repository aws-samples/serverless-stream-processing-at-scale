## Enrich Data

In this module, you'll see how you can enrich incoming streaming data with pre-stored metadata. In this case, the device data is enriched with information such as who manufactured the device, based on device ID. 

### What was created

The CloudFormation template that you ran during Set Up deployed the following:

* A **Kinesis Firehose** ingesting de-identified data.
* A **Enrich** Lambda function that looks up the metadata in Dynamo, and writes the enriched message back into the Kinesis Firehose.
* A **DeviceDetails** DynamoDB table with metadata.
* An **S3 bucket** to store the enriched data from Kinesis.

### Monitor the Pipeline
To allow you to more easily monitor this section of the pipeline, we created a CloudWatch dashboard that displays Lambda invocations, Kinesis Firehose records, and DynamoDB table reads.

1. Go to the **CloudWatch** console, go to **Dashboards**, and click on the **StreamingITL** dashboard. 

1. After a few minutes, you'll see points starting to show up in the dashboard. 

1. You can also confirm that the pipeline is working by checking S3 for transformed records.

1. Go to the **S3** console, and click on the *yourinitials*-sensor-data bucket.

1. You should see two folders: **de-identified** and **enriched**. In each of these folders, you will see the de-identified data and the data enriched with device metadata respectively. These files were PUT here by Kinesis Firehose.

	Kinesis Firehose batches incoming messages into files according to buffer size (MB) or time threshold (s), whichever is reached first. In this case, we chose to post a new batch file to S3 every 100 MB of data or every 300 seconds (5 minutes).

	Kinesis Firehose also PUTs the data into S3 in the following datetime file structure: `year/month/day/hour/`, so you will need to click into several folders before reaching the data file(s).

1. Once you reach a data file, you can download it to view the contents. You should see that the file has JSON data with the patient's **PHI/PII** (name, date of birth, temperature, oxygen percentage) **nulled out**. Additionally, in the **enriched data** folder, you will see the additional attributes: manufacturer, model.

### Next

:white_check_mark: Continue to the second module: [Detect Anomalies][detect-anomalies].

[kdg-help]: https://awslabs.github.io/amazon-kinesis-data-generator/web/help.html
[kdg]: https://awslabs.github.io/amazon-kinesis-data-generator/web/producer.html
[detect-anomalies]: ../3_DetectAnomalies/