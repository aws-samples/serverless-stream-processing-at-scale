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

1. Make sure you're in the **Oregon** Region by checking the Region dropdown in the top right corner.
   
1. Click **Create Stack**.

1. Under **Specify template**, insert this **Amazon S3 URL**: `https://serverless-stream-processing.s3-us-west-2.amazonaws.com/architecture.yaml`

1. Click **Next**.

1. Type in a **Stack name** - something like **Streaming-Workshop**.

1. Under **Parameters**, type in an **Email** that you have access to, and a unique **S3 Bucket Name**. 

	*Note that S3 Bucket names are globaly unique, so if you have the same initials as another participant, you may want to use your full name to ensure your bucket name is unique.*

1. Click **Next** twice, until you get to the **Review** page.

1. Scroll to the bottom and check all three acknowledgement boxes.

1. Click **Create stack**.

1. You will get an email at the address you provided. It will be titled **AWS Notification - Subscription Confirmation** from **devicemanufacturer**. Click **Confirm subscription** when you get the email. If you don't receive it within a few minutes, check your spam folder.

1. The stack will take a few minutes to deploy. In the meantime, you can review the architecture diagram or start reading the instructions for the first module. 

1. You can begin the first module when the stack status is **CREATE_COMPLETE**.

### Next

:white_check_mark: Continue to the first module: [Collect & De-Identify Data][collect-deidentify].

[cloudformation]: https://aws.amazon.com/cloudformation/
[collect-deidentify]: ../1_CollectDeIdentify/