Title: Persistent Storage for EC2 with Elastic Block Store
Date: 2008-08-24 16:09
Author: James
Tags: AWS
Slug: ec2-elastic-block-store

Amazon has announced a major new feature for their Elastic Compute Cloud
(EC2) service: [Elastic Block Store][] (EBS) persistent storage volumes.

EBS provides for block level storage space that can be attached to your
EC2 instances, but which exists separately from these instances and
persists even if an instance fails or is shut down. The storage volumes
can be up to 1 TB in size, can be assigned to any one of your instances
on-demand, and can be easily backed up as a snapshot to S3.

The EBS mechanism will make it significantly easier to store data
reliably on EC2 instances, removing one of the main pain points of using
EC2 instead of a standard data centre.

I don't yet have much experience with EBS myself but there is a wealth
of information available for EC2 users in the posts listed below, and
third-party tools and libraries like [ElasticFox][], [Typica][] and
[boto][] have been updated to support the storage volumes.

-   The announcement: [Amazon EBS (Elastic Block Store) - Bring Us Your Data][]
-   A growing list of tools and libraries that support EBS:
    [Amazon EBS - Tool and Library Support][]
-   Typically excellent, in-depth discussion of the EBS feature from the
    folks at RightScale: [Amazon’s Elastic Block Store explained][] and
    [Why Amazon’s Elastic Block Store Matters][]

  [Elastic Block Store]: http://www.amazon.com/b/ref=sc_fe_c_0_201590011_1?ie=UTF8&node=689343011&no=201590011
  [ElasticFox]: http://developer.amazonwebservices.com/connect/entry.jspa?externalID=609
  [Typica]: http://code.google.com/p/typica/
  [boto]: http://boto.googlecode.com/
  [Amazon EBS (Elastic Block Store) - Bring Us Your Data]: http://aws.typepad.com/aws/2008/08/amazon-elastic.html
  [Amazon EBS - Tool and Library Support]: http://aws.typepad.com/aws/2008/08/amazon-ebs---to.html
  [Amazon’s Elastic Block Store explained]: http://blog.rightscale.com/2008/08/20/amazon-ebs-explained/
  [Why Amazon’s Elastic Block Store Matters]: http://blog.rightscale.com/2008/08/20/why-amazon-ebs-matters/
