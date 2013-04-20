Title: JetS3t 0.7.4
Date: 2010-07-19 22:23
Author: James
Tags: AWS, JetS3t
Slug: jets3t-0-7-4

The latest release of JetS3t, [version **0.7.4**][], was released over
the weekend.

Bug fixes:

-   Shell scripts are more compatible with Cygwin

New toolkit functionality:

-   Added support for the new [Reduced Redundancy Storage (RRS)][] class
    for objects
-   CloudFrontService: Support for **HTTPS-only distributions** and
    logging of streaming distributions
-   Added support for buckets located in the Asia Pacific (Singapore)
    location "ap-southeast-1"
-   Improved compatibility with Eucalyptus/Walrus

Cockpit application updates:

-   Reduced Redundancy Storage class
-   Buckets located in the Asia Pacific (Singapore) location
-   HTTPS-only CloudFront distributions

Synchronize application updates:

-   Allow synchronization with third-party buckets that are not owned by
    the user

Other notes:

-   CloudFrontService API changes may break backwards-compatibility
-   SOAPService is deprecated and will soon be removed from the toolkit

Visit the JetS3t web site to [download the latest release][version
**0.7.4**] and view the latest [code samples][] and [API Javadoc][]. The
latest version should also be available from the official Maven2
repository by now.

Read about the complete list of changes in the [release notes][], and
visit the [development site][] to submit bug reports or help out with
the project.

  [version **0.7.4**]: http://jets3t.s3.amazonaws.com/downloads.html
  [Reduced Redundancy Storage (RRS)]: http://jets3t.s3.amazonaws.com/toolkit/code-samples.html#rrs
  [code samples]: http://jets3t.s3.amazonaws.com/toolkit/code-samples.html
  [API Javadoc]: http://jets3t.s3.amazonaws.com/api/index.html
  [release notes]: http://jets3t.s3.amazonaws.com/RELEASE_NOTES.txt
  [development site]: http://bitbucket.org/jmurty/jets3t/
