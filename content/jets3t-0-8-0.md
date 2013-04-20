Title: JetS3t 0.8.0, now with extra Google
Date: 2010-10-03 20:56
Author: James
Tags: Cloud Computing, Coding, JetS3t
Slug: jets3t-0-8-0

I have released the newest version of JetS3t, [version **0.8.0**][].

### Real Google Storage support

Amongst many other things, this release is the first to include native
support for [Google Storage for Developers][] (GS). This means that you
can now interact with GS using its own API instead of relying on its
(mostly) S3-compatible API. Take a look at the [GS sample code][].

I would like to thank the Google developers who helped make this
possible.

### Major changes -- Take care

This release includes more changes to the underlying JetS3t codebase
than I've made in a long time, hence the move to version 0.8.x. A broad
refactoring was necessary to add the brand new GoogleStorageService, and
it's related Google-specific features, in a relatively sane way.

The **advantages** of all these changes are:

-   JetS3t now has generic storage service, bucket, object, and
    multi-threading classes to simplify working with different
    providers, Amazon S3 or Google Storage
-   We have finally dropped support for JDK version 1.4 and moved to
    Java 6+, so we can take advantage of newer language and library
    features (generics, at last!)

The **disadvantages** of the rework are:

-   We have definitely broken backwards-compatibility for some folks who
    use older JDKs. Sorry about that
-   Despite our best intentions we may have broken
    backwards-compatibility in non-obvious places

This release is likely to be more buggy and less stable than you've come
to expect from JetS3t. Before you upgrade, be sure to read the full
[RELEASE_NOTES.txt][] document and do plenty of testing.

And, of course, [file bugs][] if you find any.

### Get the code

Visit the JetS3t web site to [download the latest release][version
**0.8.0**], and to view the latest [code samples][] and [API Javadoc][].

The latest version should be available from the official Maven2
repository within a few days.

### Change Summary

Here is a summary of new features and changes in this release.

Potentially backwards-incompatible changes:

-   Wide-ranging code changes made adding support for Google Storage may
    lead to API incompatibilities
-   JetS3t now requires Java 6+, it is no longer compatible with JDK 1.4
-   Changed property names:
    -   s3service.internal-error-retry-max =>
        storage-service.internal-error-retry-max
    -   s3service.stream-retry-buffer-size =>
        uploads.stream-retry-buffer-size
    -   s3service.defaultStorageClass =>
        s3service.default-storage-class

-   Removed antiquated and unsupported SOAPS3Service
-   Methods for setting and using AWS DevPay credentials moved from
    S3Service to RestS3Service
-   Deprecated a range of S3-specific classes, where provider-agnostic
    implementations are now available

New support for Google Storage provider:

-   Native Google Storage service and ACL implementations:
    GoogleStorageService, GSAccessControlList
-   Generic bucket, object, and service classes for interacting with
    either of the S3 or Google Storage services
-   Provider-agnostic multi-threaded services: ThreadedStorageService,
    SimpleThreadedStorageService
-   Almost all utility classes are compatible with both the S3 and
    Google Storage services

Bug fixes:

-   CloudFrontService: URL signing API changed to support HTTPS and RTMP
    resources, not just HTTP ones

New toolkit functionality:

-   RestS3Service: supports for bucket access policies
-   CloudFrontService: support for Default Root Object and object
    invalidation
-   FileComparer utility and JetS3t apps now uses a trailing slash to
    denote directory place-holder objects, instead of the custom
    "application/x-directory" content-type

Cockpit application updates:

-   Log in to either Amazon S3 or Google Storage services via GUI
-   Manage a CloudFront distribution's Default Root Object

Synchronize application updates:

-   Fully supports new GoogleStorageService, allowing synchronization
    with Google Storage via its native API
-   Choose target service end-point, Amazon S3 or Google Storage, with
    the --provider command argument

  [version **0.8.0**]: http://jets3t.s3.amazonaws.com/downloads.html
  [Google Storage for Developers]: http://code.google.com/apis/storage/
  [GS sample code]: http://jets3t.s3.amazonaws.com/toolkit/code-samples.html#gs-connect
  [RELEASE_NOTES.txt]: http://jets3t.s3.amazonaws.com/RELEASE_NOTES.txt
  [file bugs]: https://bitbucket.org/jmurty/jets3t/issues?status=new&status=open
  [code samples]: http://jets3t.s3.amazonaws.com/toolkit/code-samples.html
  [API Javadoc]: http://jets3t.s3.amazonaws.com/api/index.html
