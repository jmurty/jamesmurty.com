Title: JetS3t supports CloudFront private distributions
Date: 2009-11-12 00:57
Author: James
Tags: AWS, JetS3t
Slug: jets3t-cloudfront-private-distributions

Amazon has just announced a new [private content][] feature for their
CloudFront content distribution service.

This feature allows you to control access to S3 objects you distribute
through CloudFront by making them available only through specific
distributions, or by requiring the use of signed URLs that you generate
and provide to privileged users.

As of this evening the latest JetS3t codebase (available from the [CVS
repository][]) has full support for the new features, including the
ability to:

-   create and update private distributions
-   manage Origin Access Identifiers, which are required for private
    distributions
-   generate canned and custom-policy signed URLs for private
    distributions that require request signing.

These new features are not yet available in a stable packaged release
but I plan to provide the next stable version before the end of
November.

  [private content]: http://aws.typepad.com/aws/2009/11/new-amazon-cloudfront-feature-private-content.html
  [CVS repository]: https://jets3t.dev.java.net/source/browse/jets3t/
