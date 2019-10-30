## Clean Up

Since most of the architecture was created by running a CloudFormation template, you can clean up most of what you did today by deleting the CloudFormation stack. 

However, CloudFormation won't delete any S3 buckets that have data in them, so first you will need to empty the S3 bucket with the sensor data in it.

1. Go to the **S3** Console.

1. Click on the checkbox next to your *yourinitials*-sensor-data bucket. 

1. Click **Empty**.

1. Go to the **CloudFormation** Console.

1. Click on the stack you created during set up.

1. Click **Delete**.

You will also need to manually clean up any resources you created outside of the workshop CloudFormation stack. 

1. Go to the **CloudWatch** console and delete the CloudWatch Event you created to trigger the Publish Lambda function.

1. If you used the **Kinesis Data Generator** in Module 2, also delete the **Kinesis-Date-Generator-Cognito-User** stack.
