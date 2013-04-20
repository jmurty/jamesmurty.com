Title: AWS Management Console - EC2 Support
Date: 2009-01-20 11:43
Author: James
Tags: AWS
Slug: aws-management-console-ec2

In a concerted push to open up its infrastructure web services to a
wider audience, Amazon is building a web-based user interface to their
services called the AWS Management Console ([console.aws.amazon.com][]).

The initial version of the console was released earlier this month with
support for the Elastic Compute Cloud (EC2) service. At present, the
site provides a user-friendly interface for managing all the basic
components of your EC2 servers: instance lifecycles, machine images
(AMIs), attachable Elastic Block Store volumes, Elastic IPs, and
Security Group firewall settings.

You access the console using your normal Amazon AWS account credentials,
so if you already have an Amazon EC2 account you can sign in directly
without any fuss.

Amazon clearly intends great things for this tool. It will "soon" be
extended to support additional Amazon services: data storage with S3,
content distribution with CloudFront, messaging with SQS, and database
querying with SimpleDB. There are also plans to provide some of the
complex server and scaling management features that are the ultimate
goals of many cloud-computing users:

> **Monitoring, Load Balancing and Auto-scaling** -- View real-time
> monitoring of operational metrics within Amazon EC2, configure load
> balancing and auto-scaling rules through a web-based UI.

#### Ecological Vandalism?

I must admit I am surprised that Amazon decided to build and provide
(for free) their own web UI for these services. On the one hand, the
access to powerful, easy-to-use management tools will be a boon to both
new and existing AWS users and will no doubt encourage many more people
to try their offering. On the other hand, there are a number of
third-party businesses that already provide similar web management
console tools. These businesses may not appreciate Amazon stepping on --
or thoroughly trampling -- their turf.

My understanding was that Amazon was going to provide the basic
underlying services and APIs, on top of which it would encourage
third-party developers and companies to build out a thriving ecology of
tools, services and business models. It seems to me that one of the
major business models made possible by AWS is now under significant
threat.

I guess it will lead to some vigorous competition where companies will
need to find the gaps in Amazon's offering and provide customers with
the tools and features that are still worth paying for. The RightScale
blog published a detailed and thoughtful [response along these lines][]
upon the release of Amazon's console.

Competition is a good thing. I just hope that Amazon's huge advantages
in size and inside-knowledge don't render it the ultimate and only
victor. I'm sure that Amazon has the same hopes.

  [console.aws.amazon.com]: https://console.aws.amazon.com/
  [response along these lines]: http://blog.rightscale.com/2009/01/09/amazon-launches-ec2-console/
