Title: CloudFront: A CDN for Amazon's Simple Storage Service
Date: 2008-11-19 16:32
Author: James
Tags: AWS, Coding, JetS3t
Slug: cloudfront-a-cdn-for-s3

Amazon has added a new service to their arsenal. [CloudFront][] is a
content delivery service that works closely with S3 to make public
objects in your account available through a distribution network with
edge locations in the US, Europe and Asia.

CloudFront uses two techniques to deliver your data quickly. It caches
S3 objects in the network's edge locations (for a configurable amount of
time), and automatically routes incoming requests to the edge location
nearest to the requester. If you provide content to people who are
distant from an S3 server location, this new service could significantly
improve download speeds for your users.

The price for distribution is based on the amount of data transferred
and the number of requests, with [differential pricing][] depending on
the edge location that serves the content. Bear in mind that you will
also incur the standard S3 service costs whenever an object is provided
to an edge location.

It is straight-forward to create a CloudFront "distribution" based on
one of your S3 buckets. The AWS [blog announcement][] mentions a number
of tools and libraries that include support for the new service. My own
[JetS3t][] Java library has also been updated with basic API support for
the new service, though for now you will need to download the latest
code from CVS to access this feature. If you are keen to get your hands
dirty, go [get a CVS checkout][] and review the sample code in
[org.jets3t.samples.CloudFrontSamples][].

Inevitably, there are some drawbacks to the service:

-   Only publicly readable objects can be distributed through
    CloudFront, so you cannot use access control settings or temporary
    signed URLs to limit content delivery to specific people.
-   You cannot manually (or programmatically) expire objects at an edge
    location once they have been cached. Be careful to use appropriate
    caching directives if you intend to update or remove distributed
    objects.
-   You cannot set a cache expiry time less than 24 hours, so the
    service is not appropriate for data that is frequently updated.
-   As with S3, there is no way to display a default index.html page
    when someone requests the root location of your CloudFront
    distribution. This makes it difficult to use the service as a
    complete replacement for a web server.
-   There is currently no support for request logging, though
    [account and usage][] reports are available.
-   There is not yet an edge location close to my Australian home :-(

Despite these drawbacks, CloudFront is a very promising new tool for
anyone who needs to distribute a lot of content to a broad audience.

  [CloudFront]: http://aws.amazon.com/cloudfront/
  [differential pricing]: http://aws.amazon.com/cloudfront/#pricing
  [blog announcement]: http://aws.typepad.com/aws/2008/11/distribute-your-content-with-amazon-cloudfront.html
  [JetS3t]: https://jets3t.dev.java.net/
  [get a CVS checkout]: https://jets3t.dev.java.net/source/browse/jets3t/
  [org.jets3t.samples.CloudFrontSamples]: https://jets3t.dev.java.net/source/browse/jets3t/src/org/jets3t/samples/CloudFrontSamples.java?only_with_tag=HEAD&view=markup
  [account and usage]: http://developer.amazonwebservices.com/connect/thread.jspa?threadID=26444&tstart=0
