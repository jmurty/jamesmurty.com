Title: JetS3t support for S3 Website Hosting
Date: 2011-02-17 22:08
Author: James
Tags: JetS3t
Slug: jets3t-support-for-s3-website-hostin

I have just [released code][] for JetS3t that adds API-level support for
Amazon S3's new Website Hosting feature.

With a [Website Hosting][] configuration applied to an S3 bucket, the
bucket can serve static content but will also act in a somewhat dynamic
way to serve *index* and *error* documents if someone visits URL paths
that don't match a real file.

This makes it much more feasible to serve static website content from S3
without having to worry about users receiving strange XML error messages
if they venture off the beaten track or try to access partial URL paths.
In particular, it allows you serve an *index.html* file from the root of
a bucket, just like a real web server.

To find out more read these:

-   [Host Your Static Website on Amazon S3][]
-   [New AWS feature: Run your website from Amazon S3][]
-   [Developer Guide: Hosting Websites on Amazon S3][Website Hosting]

To try out the feature in JetS3t, grab the latest [development code][]
and read the [example test code][] to see how it works.

  [released code]: http://bitbucket.org/jmurty/jets3t/changeset/6a6618f2fbff
  [Website Hosting]: http://docs.amazonwebservices.com/AmazonS3/latest/dev/index.html?WebsiteHosting.html
  [Host Your Static Website on Amazon S3]: http://aws.typepad.com/aws/2011/02/host-your-static-website-on-amazon-s3.html
  [New AWS feature: Run your website from Amazon S3]: http://www.allthingsdistributed.com/2011/02/website_amazon_s3.html
  [development code]: https://bitbucket.org/jmurty/jets3t/wiki/Build_Instructions
  [example test code]: https://bitbucket.org/jmurty/jets3t/src/6a6618f2fbff/src/org/jets3t/tests/TestRestS3Service.java#cl-540
