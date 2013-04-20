Title: Other AWS News: HIPAA Compliance, SimpleDB Batch Put
Date: 2009-04-14 05:17
Author: James
Tags: AWS
Slug: other-aws-news-hipaa-simpledb-batch-put

Other AWS news that I haven't yet mentioned...

#### HIPAA Compliance

Amazon has [announced][] a white paper:
[Creating HIPAA-Compliant Medical Data Applications with Amazon Web Services][].

My [JetS3t][] Java library is mentioned in the blog post among the tools
that allow you to easily encrypt data that you store in S3. Check out
the JetS3t website or [discussion forum][] to find out more about
transparently encrypting the data you store in S3.

#### SimpleDB Batch Put

The SimpleDB service has been updated with a new BatchPutAttributes
operation that allows you to store up to 25 items with a single HTTP
request.

Reducing the number of requests used to upload data can significantly
speed up write operations, up to two times according to a benchmark
mentioned in the [announcement][]. You can read about the new API
operation here: [BatchPutAttributes][].

  [announced]: http://aws.typepad.com/aws/2009/04/white-paper-creating-hipaacompliant-medical-data-applications-with-amazon-web-services.html
  [Creating HIPAA-Compliant Medical Data Applications with Amazon Web Services]: http://awsmedia.s3.amazonaws.com/AWS_HIPAA_Whitepaper_Final.pdf
  [JetS3t]: http://jets3t.s3.amazonaws.com/index.html
  [discussion forum]: http://groups.google.com/group/jets3t-users
  [announcement]: http://aws.typepad.com/aws/2009/03/amazon-simpledb-batch-put.html
  [BatchPutAttributes]: http://docs.amazonwebservices.com/AmazonSimpleDB/2007-11-07/DeveloperGuide/SDB_API_BatchPutAttributes.html
