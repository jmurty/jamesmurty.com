Title: New EC2 Services: Monitor, Scale and Load Balance Your Instances
Date: 2009-05-20 10:08
Author: James
Tags: AWS, Cloud Computing
Slug: ec2-monitor-scale-and-load-balance-services

Amazon recently released three major new features for their Elastic
Compute Cloud (EC2) service --
[New Features for Amazon EC2: Elastic Load Balancing, Auto Scaling, and Amazon CloudWatch][].
These beta services are immediately available to anyone with an EC2 account and
server instances located in the US (sorry EU folks, they are US-only for now).

[Amazon CloudWatch][] is a monitoring service that records resource and
performance metrics for any EC2 instances you associate with the
service, at a cost of 1.5¢ per monitored instance per hour. In addition
to providing up to 2 weeks of monitoring data to EC2 users, this service
also underpins the other two new EC2 services.

[Auto Scaling][] is a service that will automatically start or stop EC2
instances on your behalf based on conditions you specify. In other
words, this service allows you to automatically scale the computing
power available to your application in response to changing demand.

You control your instance pool by defining triggers that react to
defined conditions such as CPU load, response latency, and the number of
healthy/unhealthy instances. Auto Scaling relies on CloudWatch to supply
the metrics it needs to make scaling decisions, so every instance
managed or started by the scaling service must be registered with
CloudWatch. Happily, there is no additional cost for using Auto Scaling
beyond the CloudWatch fees.

[Elastic Load Balancing][] (ELB) rounds out the new services by
providing the ability to distribute network traffic between multiple EC2
instances. ELB routes traffic at the HTTP or TCP level to instances
within or across Availability Zones, and avoids routing traffic to
instances that have become unresponsive. The fee for ELB is 2.5¢ per
hour for each load balancer, plus 0.8¢ per Gigabyte of data transferred
through the service. You will also need to pay the CloudWatch fee for
each load-balanced instance.

These features constitute a major step forward in EC2 functionality that
will make it easier for many users to run applications reliably in the
cloud without the need to implement their own management services.
However, it is important to recognize that the services are only a first
step and there are many situations where they will not provide the
control, precision or cost-effectiveness you will need.

Some gotchas for the services in their current incarnation include:

-   CloudWatch [metrics][] are limited to the instance/machine level and
    do not provide information about individual applications. Also, some
    metrics such as response latency and instance health are only
    available when CloudWatch is combined with the Elastic Load
    Balancing service.
-   Auto Scaling does not seem to be able to terminate instances that
    are identified as unhealthy. It will compensate for unresponsive
    instances by starting others, but will not put the original instance
    out of its misery.
-   The Elastic Load Balancing service can only balance CNAME domains
    like `www.acme.com`, not top-level ones like
    `acme.com`. It also seems to limit the range of sub-1024
    ports that can be balanced to 80 and 443, and does not perform some
    advanced load balancing functions like HTTP session affinity
    management or HTTPS termination (HTTPS connections are supported,
    but only at the TCP level).
-   You will need to work with command-line tools or use the APIs
    directly, there are not yet any graphical tools available.

As RightScale's Thorsten von Eicken points out in his
[discussion of the new services][], there is still room in Amazon's ecosystem
for third-party companies to offer value-adding services that improve on the
underlying provider's offering in terms of functionality, flexibility, price
and ease of use. As Amazon extends the capabilities of EC2 these companies will
need to work harder to add value. This situation may be tough for them, but the
fierce competition will ultimately benefit customers and accelerate the
adoption of cloud services in general.

To help you get started with the new services there is a
[post in the EC2 forums][] that succinctly lists the documentation
and resources you will need.

  [New Features for Amazon EC2: Elastic Load Balancing, Auto Scaling, and Amazon CloudWatch]: http://aws.typepad.com/aws/2009/05/new-aws-load-balancing-automatic-scaling-and-cloud-monitoring-services.html
  [Amazon CloudWatch]: http://aws.amazon.com/cloudwatch/
  [Auto Scaling]: http://aws.amazon.com/autoscaling/
  [Elastic Load Balancing]: http://aws.amazon.com/elasticloadbalancing/
  [metrics]: http://docs.amazonwebservices.com/AmazonCloudWatch/latest/DeveloperGuide/arch-AmazonCloudWatch-metricscollected.html
  [discussion of the new services]: http://blog.rightscale.com/2009/05/18/amazon-load-balancing-monitoring-auto-scaling/
  [post in the EC2 forums]: http://developer.amazonwebservices.com/connect/thread.jspa?threadID=32058&tstart=50
