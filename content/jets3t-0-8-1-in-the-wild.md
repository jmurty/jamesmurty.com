Title: JetS3t 0.8.1 in the wild
Date: 2011-04-10 19:48
Author: James
Tags: AWS, Cloud Computing, Java, JetS3t
Slug: jets3t-0-8-1-in-the-wild

The newest version of JetS3t has been released and is now roaming free.
Meet [0.8.1][].

This release has been a long time coming, mainly due to my reluctance to
finish the documentation. But it's finally here and comes with some
great new features.

### Goodies

-   Support for Amazon S3's multipart uploads, both at the [API level][]
    and with a [MultipartUtils][] tool that makes it very easy to upload
    files in multiple parts.
-   Support for Amazon S3's website configuration, which makes an S3
    bucket act more like a traditional website. I'm using this new
    feature to great effect on JetS3t's new home domain
    [www.jets3t.org][].  
    The new domain is served from S3 like the old
    *jets3t.s3.amazonaws.com* version, but it works much better if you
    visit places like the [root directory][] (versus [this][]) or a
    [missing page][] (versus [that][]).  
    Now the new domain just needs some Google-juice, so please update
    your links to point to **www.jets3t.org**.
-   Massive improvements to the Synchronize application to reduce its
    memory footprint when syncing large directory hierarchies and
    improve its efficiency when comparing local and remote files.  
    Synchronize also now supports multipart uploads, so you can back up
    files larger than 5GB and improve reliability by uploading large
    files in smaller pieces (see the `upload.max-part-size`
    configuration setting in *synchronize.properties*).
-   Support for custom (non-S3) distribution origins in the CloudFront
    API. Note that these service changes are not backwards-compatible
-   A number of bug fixes and other tweaks

See the full list of changes in the [Release History][] or [Release
Notes][] documents.

### Yes Please

Visit the JetS3t web site to [download the latest packaged
release][0.8.1], view the latest [code samples][] or read the [API
Javadoc][].

Or go to the [BitBucket developer site][]<a> to access the latest code,
[report issues][] in the bug tracker, and contribute to the project.

P.S. The latest release is on its way to the official Maven2 repository
and should be available within a day or so.

  [0.8.1]: http://www.jets3t.org/downloads.html
  [API level]: http://www.jets3t.org/api/org/jets3t/service/S3Service.html#multipartStartUpload(java.lang.String,%20java.lang.String,%20java.util.Map)
  [MultipartUtils]: http://www.jets3t.org/toolkit/code-samples.html#multipart
  [www.jets3t.org]: http://www.jets3t.org
  [root directory]: http://www.jets3t.org/
  [this]: http://jets3t.s3.amazonaws.com/
  [missing page]: http://www.jets3t.org/missing
  [that]: http://jets3t.s3.amazonaws.com/missing
  [Release History]: http://jets3t.s3.amazonaws.com/downloads.html#history
  [Release Notes]: http://jets3t.s3.amazonaws.com/RELEASE_NOTES.html
  [code samples]: http://www.jets3t.org/toolkit/code-samples.html
  [API Javadoc]: http://www.jets3t.org/api/index.html
  [BitBucket developer site]: http://bitbucket.org/jmurty/jets3t
  [report issues]: https://bitbucket.org/jmurty/jets3t/issues/new
