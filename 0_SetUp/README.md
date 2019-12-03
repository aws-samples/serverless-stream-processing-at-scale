## Set Up

If you are at an event that is providing pre-set up accounts, continue to the first module.

<details>
<summary><strong>Follow these steps if you are completing this workshop by yourself, or if your event isn't using pre-set up accounts</strong></summary>

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
* Identity and Access Management (IAM)

#### Note
If you have multiple accounts to choose from...

> Use a personal account or create a new AWS account for this workshop rather than
using an organization's account to ensure you have full access to the necessary
services and to ensure you do not leave behind any resources from the workshop.

> The code and instructions in this workshop assume only one participant is using
a given AWS account at a time. If you attempt sharing an account with another
participant, you will encounter naming conflicts for certain resources. You can
work around this by either using a suffix in your resource names or using
distinct Regions, but the instructions do not provide details on the changes
required to make this work.



### Deploy CloudFormation

[AWS CloudFormation][cloudformation] allows you to deploy infrastructure by defining an architecture in a JSON or YAML template. For this workshop, you will be deploying the architecture for all three modules with one CloudFormation template, and then you will walk through a streaming pattern in each module.

1. Go to the AWS Management Console and type **CloudFormation** in the **Find Services** search bar. Click enter to go to the CloudFormation console.

1. Make sure you're in the **Oregon** Region by checking the Region dropdown in the top right corner.
   
1. Click **Create Stack**.

1. Under **Specify template**, insert this **Amazon S3 URL**: `https://serverless-stream-processing.s3-us-west-2.amazonaws.com/Source_Code/architecture.yaml`

1. Click **Next**.

1. Type in a unique **Stack name**, like **Streaming-Workshop**.

1. Click **Next** twice, until you get to the **Review** page.

1. Scroll to the bottom and check all three acknowledgement boxes.

	> The first two acknowledgements are there because the template will deploy IAM policies to allow the services in this architecture to perform their necessary actions. The third acknowledgement is because the template uses the [AWS::Serverless Transform][CFN SAM] to define Lambda functions.

1. Click **Create stack**.

1. The stack will take a few minutes to deploy. Wait until the stack status is **CREATE_COMPLETE** before starting the first module.

</details>

### Next

:white_check_mark: Continue to the first module: [Collect & De-Identify Data][collect-deidentify].

[cloudformation]: https://aws.amazon.com/cloudformation/
[CFN SAM]: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/transform-aws-serverless.html
[collect-deidentify]: ../1_CollectDeIdentify/