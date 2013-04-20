Title: JetS3t version 0.6.0 released
Date: 2008-02-07 18:12
Author: James
Tags: AWS, JetS3t
Slug: jets3t-version-060

I am pleased to announce the release of JetS3t version **0.6.0**,
available now from the [JetS3t web site][].

This release has been a long time coming (over a year since 0.5.0) and
it includes numerous bug fixes and enhancements.

Here are some highlights:

-   Support for buckets located in Europe, including the ability to
    create these buckets in Cockpit
-   Administration tasks run much faster by using more communication
    threads by default
-   Support for generating S3 POST upload forms that will allow users to
    upload data from a web browser directly to your S3 account
-   An increased range of encryption algorithms are available thanks to
    the Bouncy Castle library, and the encryption algorithm is now
    configurable in Cockpit via the Preferences dialog
-   Added a brand new application called CockpitLite, which allows you
    to provide third parties with mediated access to your S3 account via
    the Gatekeeper
-   Rudimentary bandwidth throttling for uploads
-   REST implementation now automatically adjusts for clock differences
    between a client machine and S3 (ie RequestTimeTooSkewed failures
    will be a thing of the past)
-   The Synchronize application has been made more configurable with a
    range of new options
-   Includes configuration options for requesting specific TCP window
    size settings from your kernel

Refer to the [RELEASE_NOTES.txt][] document for a full list of
enhancements.

  [JetS3t web site]: http://jets3t.s3.amazonaws.com/index.html
  [RELEASE_NOTES.txt]: http://jets3t.s3.amazonaws.com/RELEASE_NOTES.txt
