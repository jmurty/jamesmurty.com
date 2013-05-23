Title: Major S3 and SQS outage
Date: 2008-07-21 07:26
Author: James
Tags: AWS
Slug: major-s3-and-sqs-outage

As I post this, Amazon's S3 and SQS services have both been down for
hours. The latest updates to the [service health dashboard][] are
promising so things will hopefully be resolved soon, but this definitely
isn't a good sight:

![The AWS Service Health Dashboard showing that the S3 and SQS services are down][]

### Update

Amazon has posted a full explanation of the recent S3 outage here:
[Amazon S3 Availability Event: July 20, 2008][].

This makes for interesting reading, but ultimately the lesson from this
most recent outage is that service failures can and will happen. Even to
Amazon.

If you are building a cloud-based application you should try to include
as many contingency options as much as possible, but few contingencies
could have survived that outage. Let's hope it isn't repeated.

  [service health dashboard]: http://status.aws.amazon.com/
  [The AWS Service Health Dashboard showing that the S3 and SQS services are down]: http://jamesmurty.com/static/images/2008/07/aws_dashboard_s3_and_sqs_down.gif "aws_dashboard_s3_and_sqs_down"
  [Amazon S3 Availability Event: July 20, 2008]: http://status.aws.amazon.com/s3-20080720.html
