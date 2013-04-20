Title: Persistent Storage in EC2 later this year
Date: 2008-04-14 18:39
Author: James
Tags: AWS
Slug: persistent-storage-in-ec2-later-this-year

Amazon is working on a significant new feature for the EC2 service:
persistent storage. According to [this pre-announcement post][] in the
developer forums, EC2 users will be able to create storage volumes that
exist separately from individual instances, but which can be attached to
your instances on demand. These storage volumes will look like normal
block devices to your instance, meaning you can format and combine them
in any way you want.

The persistent storage feature is still in the testing stages and is not
yet available to the general public. There is more information available
on the [Amazon Web Services Blog][] and on the [RightScale blog][],
where they have access to the trial version.

A robust, flexible and reliable persistent storage mechanism could
revolutionise the EC2 service, and will definitely simplify the process
of deploying your applications to the cloud. However, I wonder whether
this feature will damage the third-party providers who already offer
persistence solutions for EC2.

As Amazon continues to develop and improve their infrastructure
services, they will need to be careful to avoid wiping out the
third-party vendor ecosystem based on these services.

  [this pre-announcement post]: http://developer.amazonwebservices.com/connect/thread.jspa?threadID=21082&tstart=0
  [Amazon Web Services Blog]: http://aws.typepad.com/aws/2008/04/block-to-the-fu.html
  [RightScale blog]: http://blog.rightscale.com/2008/04/13/amazon-takes-ec2-to-the-next-level-with-persistent-storage-volumes/
