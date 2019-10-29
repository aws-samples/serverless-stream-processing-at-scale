## Set Up

### AWS Account

In order to complete this workshop, you'll need an AWS account and permissions to access the following services:

* AWS IoT
* Lambda
* Simple Storage Service (S3)
* DynamoDB
* Key Management Service (KMS)
* Kinesis Firehose, Streams, and Analytics
* Simple Notification Service (SNS)
* CloudWatch

The code and instructions in this workshop assume only one participant is using
a given AWS account at a time. If you attempt sharing an account with another
participant, you will encounter naming conflicts for certain resources. You can
work around this by either using a suffix in your resource names or using
distinct Regions, but the instructions do not provide details on the changes
required to make this work.

Use a personal account or create a new AWS account for this workshop rather than
using an organization's account to ensure you have full access to the necessary
services and to ensure you do not leave behind any resources from the workshop.

### CloudFormation

[AWS CloudFormation][cloudformation] allows you to model your entire infrastructure with a JSON or YAML template. For this workshop, you will be deploying the architecture for all three modules with CloudFormation, and then you will walk through a streaming pattern in each module.

1. Go to the AWS Management Console and type **CloudFormation** in the **Find Services** search bar. Click enter to go to the CloudFormation console.
   
1. Click **Create Stack**.

1. Under **Specify template**, select **Upload a template file**.

1. Download TODO.yaml from this repository, and upload it to the CloudFormation console.

1. Click **Next**.

1. TODO 

### Next

:white_check_mark: Continue to the first module: [Collect & De-Identify Data][collect-deidentify].

[cloudformation]: https://aws.amazon.com/cloudformation/
[collect-deidentify]: ../1_CollectDeIdentify/