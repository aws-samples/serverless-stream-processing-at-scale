## Detect Anomalies

In this module, you'll see how you can use **Kinesis Analytics** to analyze streaming data in near real-time as it is ingested. In this case, the Random Cut Forest algorithm is used to generate anomaly scores. You'll be sent an email whenever an anomaly in the streaming data is found.

### What was created

The CloudFormation template that you ran during Set Up deployed the following:

* A **Device Data Analytics** Kinesis Analytics Application, taking **IngestStream** data as an input, and calculating anomaly_scores.
* A **OutputStream** Kinesis Firehose which takes the **Device Data Analytics** data and puts it into S3 Sensor Data bucket.
* A **Alert** Lambda function triggered from **OutputStream**, which sends an SNS notification whenever an anomaly_score above/below the threshold is found.
* A **device manufacturer** SNS Topic for email notifications

### Instructions
1. Go to the **Kinesis** console.

1. Select **Data Analytics** on the left-hand side.

1. Select the **Device Data Analytics** Kinesis Data Analytics Application.

1. Click on the **Actions** dropdown, and click **Run Application**. Confirm that you want to run the application.

1. Once it's running, click on **Application details**.

1. Under **Streaming data**, you can see that this application is taking data in from **IngestStream** and applying the **FirehoseTransform** Lambda function to enrich the data with manufacturer and model information.

1. Under **Destination**, you can see that the results are being sent to **Output Stream** to be sent to S3, as well as being sent to the **Alert** Lambda function so that anomaly scores above the threshold will trigger an SNS Email notification.

1. Click on **Go to SQL results** to see what's happening in real-time.

1. Under the **Source** tab, you can see incoming records from **IngestStream**. If you see the message **No rows in source stream**, this means that there aren't any incoming records at that moment. That may happen due to Kinesis Firehose buffering data, or since the Publish Lambda function only runs every minute. Wait a few seconds and try again by clicking **Retrieve rows**.

1. Click on the **Real-time Analytics** tab.

1. In either **DEST_STREAM**, you should see data rows including an **ANOMALY_SCORE** that was calculated using the Random Cut Forest algorithm.

1. You can confirm that there is now an **anomaly_scores** folder in the S3 bucket with the same data you see in the **DEST_STREAMs**.

1. If an anomaly score is returned above the threshold, you will be emailed at the email you provided during set up.

1. The threshold was determined by collecting anomaly_scores from a sample data set and finding the mean anomaly_score. The chosen threshold is three standard deviations above/below the mean.

1. You should notice that the **pulse** in the email alerts sent to you tend to be low (below 60). This is because the simulated data coming in usually reports pulse in the range of 60-120 but occassionally sends a pulse below 60. This is an anomaly that Kinesis Analytics has picked up on!

### Next

:white_check_mark: [Clean Up][cleanup].

[cleanup]: ../4_CleanUp/