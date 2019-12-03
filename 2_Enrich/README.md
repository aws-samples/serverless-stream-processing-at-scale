## Enrich Data

In this module, you'll see how you can enrich incoming streaming data with pre-stored metadata. This is helpful for a few reasons. One, with IoT devices sending data so frequently, you want to limit the size of your payloads and not send any data you don't strictly need to. Two, if there is data related to the incoming device data that would aide real-time analytics, it can be added in at this stage, after the data has been ingested into AWS. In this case, the device data is enriched with information such as who manufactured the device. This information can be used later to inform manufacturers if their devices are experiencing anomalies.

### What was Created

The CloudFormation template deployed the following:

![Module 2 Architecture](Screenshots/arch-mod2.png)

* A **Kinesis Firehose** ingesting de-identified data from the **De-Identify** Lambda function (from Module 1).
* A **Enrich** Lambda function that looks up the metadata in Dynamo, and writes the enriched message back into the Kinesis Firehose.
* A **DeviceDetails** DynamoDB table with metadata.
* An **S3 bucket** to store the de-identified and enriched data from Kinesis.

### Monitor the Pipeline
To allow you to more easily monitor this section of the pipeline, a **CloudWatch dashboard** was created that displays Lambda invocations, Kinesis Firehose records, and DynamoDB table reads.

1. Go look at the **StreamingITL** dashboard.

	<details><summary><strong>Step by Step Instructions</strong></summary>

	1. Go to the **CloudWatch** console.

	1. Go to **Dashboards**

	1. Click on the **StreamingITL** dashboard. 

		> You may have to wait a few minutes depending on when you started publishing data in the previous module, but soon you'll see points starting to show up in the dashboard. 

		> Click the refresh button in the top right corner as needed until data starts to appear.
		
	</details>

	Now you can see how fast data is coming in, and you can keep an eye out for any errors or throttling events. 

	Here is an example from a pipeline that has been running for a few hours:

	![Dashboard](Screenshots/dashboard.png)

1. Confirm that the pipeline is working by checking S3 for transformed records.

	<details><summary><strong>Step by Step Instructions</strong></summary>

	1. Go to the **S3** console.

	1. Click on the **sensor-data-XXXXXXXX** bucket

		> The random suffix is there to ensure your bucket name is globaly unique, as [required by S3][s3-bucket-name].

	1. You should see two folders: **de-identified** and **enriched**. In each of these folders, you will see the de-identified data and the data enriched with device metadata respectively. These files were PUT here by Kinesis Firehose.

	</details>

	Kinesis Firehose batches incoming messages into files according to buffer size (MB) or time threshold (s), whichever is reached first. In this case, we chose to post a new batch file to S3 every 1 MB of data or every 60 seconds.

	Kinesis Firehose also PUTs the data into S3 in the following datetime file structure: `year/month/day/hour/`, so you will need to click into several folders before reaching the data file(s).

	> You may also see a **processing-failed** folder under the **de-identified** and/or **enriched** folders. 
	
	<details><summary><strong>Read More</strong></summary>
	
	Any records that could not be properly processed by Kinesis are sent to a **processing-failed** subfolder. 
	
	This may be due to your Lambda concurrent invocation limit being too low (default soft limit is 1,000), or a failure from the lambda function itself.
	
	This is very helpful for **auditing** purposes. 
	
	> **Hint**: if throttling is to blame, there is a helpful dashboard to see if that is the case...
	
	> You can also go to the Monitoring page and CloudWatch logs for the **FirehoseTransform** lambda function to investigate.
	
	</details>

1. Download one of the data files to view the contents.

	<details><summary><strong>Step by Step Instructions</strong></summary>

	1. Click through the folder structure until you reach a data file.

	1. Select the **checkbox** to the left of the data file.

	1. Click on the **Download** button.

		![S3 Contents](Screenshots/s3-content.png)

	1. You should see that the file has JSON data with the patient's **PHI/PII** (name, date of birth, temperature, oxygen percentage) **nulled out**. Additionally, in the **enriched data** folder, you will see the additional attributes: manufacturer, model.

		Here is an example from an **enriched** file:

		![Enriched File](Screenshots/enriched.png)
	
	</details>

### Next

:white_check_mark: Continue to the third module: [Detect Anomalies][detect-anomalies].

[s3-bucket-name]: https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-s3-bucket-naming-requirements.html
[kdg-help]: https://awslabs.github.io/amazon-kinesis-data-generator/web/help.html
[kdg]: https://awslabs.github.io/amazon-kinesis-data-generator/web/producer.html
[detect-anomalies]: ../3_DetectAnomalies/