Title: EC2: Out of beta, adds an SLA and Windows!
Date: 2008-10-24 10:57
Author: James
Tags: AWS
Slug: ec2-out-of-beta-adds-an-sla-and-windows

Amazon has [announced a major update][] to EC2, its service that
provides on-demand computing power.

The service has graduated from "beta" to production level, which means
that a [Service Level Agreement][] is now available. If you experience
uptime below 99.95% in a given month and you can provide supporting
evidence, Amazon will provide a 10% service credit for that month's
bill.

Even more interesting is the news that you can now run Windows Server
2003 and SQL Server on EC2 instances. Amazon's [Windows on EC2
documentation][] lists the prices for running these instances: from
12.5¢ per hour for a small instance with Windows only, and from $1.35
per hour for an instance with Windows, SQL Server, and Authentication
Services. See the [Windows AMIs][] listing for more details.

Understandably, Windows instances on EC2 work very differently than the
Linux ones. The folks at RightScale have published a [blog post][]
describing some of the differences and quirks of the Windows instances.

Although I much prefer "Unixy" platforms for my own development, I can
imagine situations where it would be very handy to have a Windows
machine easily available -- such as for running those vital but
irritating programs that are only made available for Windows. Australian
Tax Office, I'm [looking at you...][]

To take advantage of the new Windows instances, download the latest
version of the [ElasticFox Firefox Extension][] and be sure to check out
the [Elasticfox Manual (PDF)][].

  [announced a major update]: http://aws.typepad.com/aws/2008/10/big-day-for-ec2.html
  [Service Level Agreement]: http://aws.amazon.com/ec2-sla
  [Windows on EC2 documentation]: http://aws.amazon.com/windows/
  [Windows AMIs]: http://developer.amazonwebservices.com/connect/kbcategory.jspa?categoryID=209
  [blog post]: http://blog.rightscale.com/2008/10/23/amazon-ec2-windows-sla/
  [looking at you...]: http://www.ato.gov.au/individuals/content.asp?doc=/content/32234.htm&pc=001/002/014/011/001&mnu=&mfp=&st=&cy=1
  [ElasticFox Firefox Extension]: http://developer.amazonwebservices.com/connect/entry.jspa?externalID=609
  [Elasticfox Manual (PDF)]: http://developer.amazonwebservices.com/connect/entry.jspa?externalID=1797
