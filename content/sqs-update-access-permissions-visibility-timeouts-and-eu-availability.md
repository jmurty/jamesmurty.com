Title: SQS Update: Access permissions, visibility timeouts, and EU availability
Date: 2009-04-14 04:59
Author: James
Tags: AWS
Slug: sqs-update-access-permissions-visibility-timeouts-and-eu-availability

Amazon's SQS messaging service has been updated with some interesting
new features, as announced in the AWS blog post [Powerful New Amazon SQS
Features][].

#### Access Permissions

The original release of SQS allowed users to set access permissions for
their message queues so that third-parties could participate in their
messaging system. This feature was deprecated by Amazon in the
2008-01-01 version of the service's API due to unspecified shortcomings
in the way the access was handled. Since then, users who relied on queue
sharing capabilities for their applications needed to continue using the
older API which was due to expire on May 6 this year.

In the new SQS API version 2009-02-01, the service's ability to share
queues has been reinstated along with a greatly improved access control
model. The [Shared Queues][] feature allows you to grant third-parties
access to your message queues using either simple API calls to control
principal-based permissions (for other AWS account-holders) or by
writing more sophisticated rules using a new Access Policy Language. The
policy language provides many more features, including the ability to
grant public access or to limit access based on IP address ranges.

#### Visibility Timeouts

Another feature that was lost in the 2008-01-01 API update was the
ChangeMessageVisibility operation, which allowed users to change the
visibility timeout for a specific message on-demand as well as when the
message was delivered. This feature was very useful for delaying the
redelivery of a message when it turned out that your application would
not be able to process the original message as quickly as expected, a
common occurrence in applications that process work units with
unpredictable processing times.

This feature too has been reinstated in the new API version under the
same name: [ChangeMessageVisibility][]. With this operation you can
change/extend a message's visibility timeout up to 12 hours.

#### EU Availability

SQS has now joined the list of services with endpoints located in
Europe, which will make the service perform better for users in that
part of the world. This is particularly good news for anyone running EC2
instances in the EU region, because data traffic between these instances
and EU-based SQS queues is free.

#### Read more

There is a lot to like in this service update. See the full list of
changes, and detailed documentation, in the Amazon Simple Queue Service
[Developer Guide][].

  [Powerful New Amazon SQS Features]: http://aws.typepad.com/aws/2009/04/powerful-new-sqs-features.html
  [Shared Queues]: http://docs.amazonwebservices.com/AWSSimpleQueueService/2009-02-01/SQSDeveloperGuide/acp-overview.html
  [ChangeMessageVisibility]: http://docs.amazonwebservices.com/AWSSimpleQueueService/2009-02-01/SQSDeveloperGuide/Query_QueryChangeMessageVisibility.html
  [Developer Guide]: http://docs.amazonwebservices.com/AWSSimpleQueueService/2009-02-01/SQSDeveloperGuide/
