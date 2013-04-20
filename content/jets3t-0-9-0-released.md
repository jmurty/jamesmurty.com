Title: JetS3t 0.9.0 Released
Date: 2012-03-12 23:02
Author: James
Tags: AWS, Java, JetS3t
Slug: jets3t-0-9-0-released

The newest version of JetS3t has been released and is now available for
download: [JetS3t 0.9.0][]

This release has been a long time coming, sorry about that. I had
intended to get a release out late last year but personal factors left
me short of time: relocating back to Australia from the U.S. and helping
out with our newly-arrived baby boy have kept me pretty busy.

Still, the 0.9.0 version is now official. Here are some of the major new
features and improvements.

### HttpComponents Upgrade

A major change in the new version is JetS3t's use of the newer 4.x
generation of the key [HttpClient library][] (now more accurately called
HttpComponents). The older HttpClient 3.x had been end-of-lifed and
while it still worked fine, relying on the obsolete version was not a
good long-term option.

I need to thank two contributors in particular for doing a lot of this
work. Cheers to [Gilles Gaillard][] and [David Kocher][] for their
invaluable work; the upgrade wouldn't have happened without them.

Note that since this upgrade involved updates to the core JetS3t HTTP
code layer, there is a risk of subtle bugs in the HTTP handling with
this release. I think the risk is small and some people have been using
the pre-release 0.9.0 code successfully for a while now, but when you
update to 0.9.0 it's worth doing a little more testing than you might
normally.

Here are some of the new service-specific features.

### Amazon S3

-   Support for multiple object deletes in a single request
-   Explicit support for new S3 locations: Oregon (`us-west-2`), South
    America (`sa-east-1`), GovCloud US West (`s3-us-gov-west-1`),
    GovCloud US West FIPS 140-2 (`s3-fips-us-gov-west-1`)
-   Support for server-side encryption, with per-object setting of
    algorithm and default algorithm configuration with the new
    `s3service.server-side-encryption` property
-   Support for Multipart Upload Part - Copy operation, to add data from
    existing S3 objects to multipart uploads.
-   Support for signing S3 requests with response-altering request
    parameters like `response-content-type` and
    `response-content-disposition`

### Google Storage

-   Support for OAuth2 authentication mechanism, with automatic access
    token refresh.

### Conclusion

Please grab the latest version, try it out and let me know how it goes.

Visit the JetS3t web site to [download the latest packaged
release][JetS3t 0.9.0], view the [code samples][] or read the [API
Javadoc][].

For a more complete list of changes see the [Release History][] or
[Release Notes][] documents.

Or go to the [BitBucket developer site][] to access the latest code,
[report issues][] in the bug tracker, and contribute to the project.

P.S. The latest release is on its way to the official Maven2 repository
and should be available within a day or so.

  [JetS3t 0.9.0]: http://www.jets3t.org/downloads.html
  [HttpClient library]: http://hc.apache.org/index.html
  [Gilles Gaillard]: https://bitbucket.org/gillouxg
  [David Kocher]: https://bitbucket.org/dkocher
  [code samples]: http://www.jets3t.org/toolkit/code-samples.html
  [API Javadoc]: http://www.jets3t.org/api/index.html
  [Release History]: http://jets3t.s3.amazonaws.com/downloads.html#history
  [Release Notes]: http://jets3t.s3.amazonaws.com/RELEASE_NOTES.html
  [BitBucket developer site]: http://bitbucket.org/jmurty/jets3t
  [report issues]: https://bitbucket.org/jmurty/jets3t/issues/new
