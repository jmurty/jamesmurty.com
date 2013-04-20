Title: JetS3t support for S3 Versioning (Beta)
Date: 2010-01-20 01:30
Author: James
Tags: AWS, JetS3t
Slug: jets3t-s3-versioning

Amazon is working on an interesting new feature for the S3 service:
Object versioning.

Once you enable versioning for one of your S3 buckets, any time you
change an object in that bucket a version of the prior object will be
stored in addition to the latest one. You can then perform operations on
prior object versions such as retrieving older data, restoring "deleted"
objects, and generally maintaining a fail-safe history of everything
that happens in the bucket.

This will be a boon to anyone who is worried about their S3 data being
accidentally deleted or corrupted by user/computer error.

The feature is currently in early beta form and is available for testing
with buckets located in the "us-west-1" location. You can read about the
current functionality here: [Versioning Beta Design][].

Better still, you can grab the [latest JetS3t code][] from CVS and try
it out for yourself! The code samples file [CodeSamples.java][] now
includes a section called "Bucket Versioning (Beta)" to get you started.

Both the versioning feature itself and JetS3t's support for it are in an
early stage so watch out for warts.

  [Versioning Beta Design]: http://doc.s3.amazonaws.com/betadesign/Versioning.html
  [latest JetS3t code]: https://jets3t.dev.java.net/source/browse/jets3t/
  [CodeSamples.java]: https://jets3t.dev.java.net/source/browse/jets3t/src/org/jets3t/samples/CodeSamples.java?rev=1.29&view=markup
