Title: Two New EC2 Instance Types with more CPU Power
Date: 2008-05-30 10:21
Author: James
Tags: AWS
Slug: new-ec2-high-cpu-instance-types

Amazon has [announced][] the availability of two new Elastic Compute
Cloud (EC2) instance types with increased CPU processing power, bringing
the total number of instance types to five.

The new instances are termed "High-CPU" versions, and they have a focus
on raw processing power as measured in EC2 Compute Units (ECUs). The
following table puts the new `c1.medium` and `c1.xlarge` instances in
perspective:

  Name        ECUs   Memory   Storage   Platform   Hourly Price
  ----------- ------ -------- --------- ---------- --------------
  m1.small    1      1.7 GB   160 GB    32-bit     10¢
  c1.medium   5      1.7 GB   350 GB    32-bit     20¢
  m1.large    4      7.5 GB   850 GB    64-bit     40¢
  c1.xlarge   20     7 GB     1690 GB   64-bit     80¢
  m1.xlarge   8      15 GB    1690 GB   64-bit     80¢

For a more detailed overview of the instance types available in EC2, see
the [Instance Types][] section in the service's API documentation.

  [announced]: http://aws.typepad.com/aws/2008/05/more-ec2-power.html
  [Instance Types]: http://docs.amazonwebservices.com/AWSEC2/2008-02-01/DeveloperGuide/instance-types.html
