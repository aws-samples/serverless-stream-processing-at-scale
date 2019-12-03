## Serverless Stream Processing at Scale

In this workshop, you will explore several patterns for stream processing at scale in AWS. The methods used here are based on the [Serverless Streaming and Architecture Best Practices White Paper][whitepaper].

Imagine that you are at a health care company that deploys equipment in hospitals across the globe. The equipment collects patient data, and you need to ingest and analyze the data at scale, in near real-time, in a HIPAA compliant manner. 

In this workshop, you will deploy and explore the architecture below, which takes in simulated life support device sensor data and processes it. The entire architecture is [serverless][serverless] and uses [HIPAA-eligable services][compliance].

![Architecture Diagram](architecture-diagram.jpg)

### Workshop Structure

This workshop is divided into three modules that are meant to be completed **in order**.

You will not deploy the architecture manually. Instead, you will be able to explore the architecture, understand architecture patterns, and apply changes as necessary.

If you are already familiar with the services in question, as an **extra challenge**, try to complete the workshop without reading the **step-by-step instructions** provided in the dropdowns.

Whatever level you're at, make sure you read the workshop fully to get the most out of it. And, if you finish ahead of time, feel free to change or add onto the pipeline to see what happens!

> If you are using an account that was pre-set up for this workshop, you will have limited permissions, and may not be able to alter certain aspects of the pipeline.

### Modules

| | Module | Description |
| --- | :---: | :--- |
| 0 | [Set Up][setup] | Deploy the architecture using a [CloudFormation][cloudformation] template. |
| 1 | [Collect & De-Identify Data][collect-deidentify] | Ingest simulated real-time device data into [IoT Core][iotcore], de-identify the data using an IoT [Lambda][lambda] Action, saving the PHI/PII data to an encrypted [DynamoDB][dynamo] table while sending PHI/PII-free data on to [S3][s3] via [Kinesis Firehose][firehose]. |
| 2 | [Enrich Data][enrich] | Enrich streaming data using a [Kinesis Firehose][firehose] Record Transformation with metadata from [DynamoDB][dynamo], and then store the enriched records in [S3][s3]. |
| 3 | [Detect Anomalies][detect-anomalies] | Use [Kinesis Analytics][analytics] to calculate anomaly scores with the Random Cut Forest algorithm, and automatically send an [SNS][sns] text message if an anomaly is found. |
| 4 | [Clean Up][clean-up] | Delete the entire architecture. |

[whitepaper]: https://d1.awsstatic.com/whitepapers/Serverless_Streaming_Architecture_Best_Practices.pdf
[serverless]: https://aws.amazon.com/serverless/
[compliance]: https://aws.amazon.com/compliance/services-in-scope/
[cloudformation]: https://aws.amazon.com/cloudformation/
[iotcore]: https://aws.amazon.com/iot-core/
[lambda]: https://aws.amazon.com/lambda/
[dynamo]: https://aws.amazon.com/dynamodb/
[s3]: https://aws.amazon.com/s3/
[firehose]: https://aws.amazon.com/kinesis/data-firehose/
[analytics]: https://aws.amazon.com/kinesis/data-analytics/
[sns]: https://aws.amazon.com/sns/
[setup]: 0_SetUp/
[collect-deidentify]: 1_CollectDeIdentify/
[enrich]: 2_Enrich/
[detect-anomalies]: 3_DetectAnomalies/
[clean-up]: 4_CleanUp/
