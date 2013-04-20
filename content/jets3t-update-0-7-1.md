Title: JetS3t Update: 0.7.1
Date: 2009-05-10 10:27
Author: James
Tags: AWS, Java, JetS3t
Slug: jets3t-update-0-7-1

JetS3t (jet-set) version **0.7.1** is now available. This is the latest
version of my open source Java S3 library and application suite.

Visit the JetS3t web site to download the new version, run the updated
online applications, or read the latest documentation:
<http://jets3t.s3.amazonaws.com/index.html>

This version includes bug fixes and support for the CloudFront service's
new [Access Logs][] feature. Access logs allow you to record the
activity within your CloudFront distributions and save the information
to log files in one of your S3 buckets. See the [Amazon CloudFront
Request Logging][] blog post for more details.  
<!--more-->  
Bug fixes:

-   REST implementation was mistakenly limited to 20 simultaneous
    connections
-   Removed a menu display bug in Cockpit that caused the bucket and
    object action menus to appear behind other GUI elements.

New toolkit functionality:

-   Support for the Amazon CloudFront service's Access Logging feature
-   JMX Instrumentation
-   JetS3t property httpclient.max-connections now sets the global
    connection limit, while the new property
    httpclient.max-connections-per-host (optional) sets the per-host
    connection limit
-   Added simplified constructors for S3Object, so the object's bucket
    need not be specified in advance
-   Improved compatibility with the Eucalyptus/Walrus storage service.

Cockpit application updates:

-   Manage Access Logging settings for your CloudFront distributions
-   New "Switch login" Service menu item for users with multiple S3
    accounts.

  [Access Logs]: http://docs.amazonwebservices.com/AmazonCloudFront/latest/DeveloperGuide/AccessLogs.html
  [Amazon CloudFront Request Logging]: http://aws.typepad.com/aws/2009/05/amazon-cloudfront-request-logging.html
