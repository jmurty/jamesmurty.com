Title: Major S3 and AWS outage leaves us in the dark in more ways than one
Date: 2008-02-16 09:40
Author: James
Tags: AWS
Slug: major-s3-and-aws-outage-leaves-us-in-the-dark-in-more-ways-than-one

A number of Amazon's AWS services suffered a massive outage earlier
today. For some customers, the S3 data storage service was unavailable
for hours.

The [forum thread][] where this drama played out makes for some
interesting reading. Most notable is the ongoing clamour of users for
information from Amazon staff about the issue, and the sparsity of
official feedback during the crisis.

This thread highlights an important shortcoming of the AWS offering,
quite apart from the outage itself. Amazon does not offer a central web
page location that gives the current status of AWS services, nor is
there any other kind of notification mechanism to let users know if the
services are struggling and what Amazon is doing in response. Once users
notice a fault, they must visit the developer discussion forums to see
whether the fault is unique to them, to notify Amazon staffers of their
issue, and to seek feedback.

For infrastructure services that are a vital component of many
businesses, a discussion forum is in no way a sufficient communication
channel for fault notifications and tracking. Especially as users were
locked out of the forums themselves for a period during the outage.

Amazon needs to do better.

#### Update

It looks like Amazon have recognized that their forums are an inadequate
fault notification and monitoring system, and they have started work on
an alternative. From the forum:

> Additionally, we’ve begun work on a service health dashboard, and
> expect to release that shortly.

Details are scarce, but this is a promising development.

  [forum thread]: http://developer.amazonwebservices.com/connect/thread.jspa?threadID=19714
    "S3 Forum discussing the outage"
