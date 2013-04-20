Title: Big data + Little pipe? Try S3 Ingestion
Date: 2009-05-27 13:33
Author: James
Tags: AWS, Cloud Computing
Slug: s3-ingestion

A major barrier to moving your data to an online storage location like
[Amazon's S3][] can be the time it takes to push large numbers of bytes
through your upstream Internet connection. While your connection may be
fast enough to keep your data fresh and in-sync from day to day, it can
be painful to do the initial data load if you have huge files, very many
smaller files, a slow connection, or some combination of these factors.

I feel your pain. For the longest time I risked losing all my precious
music files because I didn't want to flood my home Internet bandwidth
for the *four whole days* it would take to upload them all.

Amazon is aiming to address this issue with the new AWS Import/Export
service, currently in limited beta in the United States.  
<!--more-->  
[AWS Import/Export][] is a pragmatic low-tech solution to the problems
of uploading huge amounts of data. You save your data to one or more
physical hard drives, then ship these drives directly to Amazon where
their contents will be read and copied into your own S3 account. When
the data is loaded, Amazon will ship the drive back to you.

#### Some Details

You provide data loading instructions and authenticate your hard drive
by sending a manifest file to Amazon in advance, then include a
digitally signature of this manifest on the drive itself. Not all drive
types are supported, so be sure to check the list of [supported
devices][] before you ship your drive.

The time to load your data into S3 will vary greatly based on the speed
of your drive and the amount of data, but it is worth noting that this
service is not yet a solution for urgently loading data. Amazon will
generally only start reading your drive the next business day after it
arrives, so you should expect to wait at least a couple of business days
from sending your drive until your data is available in S3. The
service's home page contains a handy table that gives guidance about
when AWS Import/Export is likely to be faster than using the [series of
tubes][].

The service costs $80 US per drive processed, with additional fees of
$2.49 per hour the service spends reading the drive plus the standard
S3 request and storage fees. Because the data is loaded over Amazon's
internal network instead of the Internet, there are no data transfer
fees.

Check out the [service announcement blog post][] for pointers to tools
that work with the new service, and to a calculator for comparing costs
for Internet vs. physical data loads.

#### Something Missing?

Although this new service is named Amazon Import/Export, only the first
part of that duo is currently available. There is not yet any way to
export data from S3 on physical drives. This feature is obviously in the
works, but there is no timetable for its release.

  [Amazon's S3]: http://aws.amazon.com/s3
  [AWS Import/Export]: http://aws.amazon.com/importexport/
  [supported devices]: http://aws.amazon.com/importexport/#supported_devices
  [series of tubes]: http://www.google.com/url?sa=t&source=web&ct=res&cd=1&url=http%3A%2F%2Fen.wikipedia.org%2Fwiki%2FSeries_of_tubes&ei=L58dSvT6HYXAswPr8cSKCg&usg=AFQjCNHdJsGnyTipISFGyeER5jfAAy8VMg&sig2=YgVJVZkfv6a1uasRwSo5aA
  [service announcement blog post]: http://aws.typepad.com/aws/2009/05/send-us-that-data.html
