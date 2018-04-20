Title: JetS3t: S3 Versioning, Multi-Factor Authentication and BitBucket
Date: 2010-02-08 23:53
Author: James
Tags: AWS, JetS3t
Slug: jets3t-s3-versioning-and-mfa

There is a lot of S3 and JetS3t news tonight.

### Versioning For All

To begin with, the new S3 [beta versioning][] feature is [now available
in all regions][]. This means that you can retain past versions of all
your S3 objects regardless of where your bucket is located.

The latest JetS3t code has full support for versioning that makes it
very easy to use. You can enable versioning for a bucket like so:

    :::java
    restS3Service.enableBucketVersioning("bucket-name");

Then should you ever need to recover some data -- such as after
accidentally deleting an object or overwriting data with a corrupted
file -- you can find and retrieve the prior versions:

    :::java
    // List an object's prior versions
    BaseVersionOrDeleteMarker[] versions = restS3Service
        .getObjectVersions("bucket-name", "object-name");

    // Retrieve the next-to-last version of data
    String versionId = versions[versions.length - 2].getVersionId();
    S3Object priorVersionObject = s3Service.getVersionedObject(
        versionId, "bucket-name", "object-name");

### The Second Factor

As well as rolling out broader availability of the versioning feature
Amazon has (somewhat quietly) added another interesting feature: the
first API-level support for multi-factor authentication. Multi-factor
authentication (MFA) adds an extra level of security to systems by
requiring users to prove ownership of a token or device of some kind in
addition to their normal login credentials. This means that even if
someone steals or guesses your credentials they will be unable to
perform actions on your account because they do not possess the device.

In Amazon's case, like PayPal and some banks before them, the additional
factor comprises a small electronic device that generates code numbers.
Once you have [purchased one of these devices][] and enabled it in your
AWS account you will be required to provide an extra code number when
performing certain tasks.

Previously the additional MFA device code was only required when you
logged in to the [AWS Console][] but as of today you can turn on MFA for
your S3 buckets in tandem with versioning. When versioning with MFA is
enabled not only will the bucket's owner be the only user who can
permanently delete object versions, but this user will be required to
provide a time-limited MFA code to do so.

Again, this is relatively straight-forward to use in JetS3t:

    :::java
    // Require MFA to permanently delete object versions
    restS3Service.enableBucketVersioningWithMFA("bucket-name");

    // Obtain user's MFA device serial number and time-limited code
    String multiFactorSerialNumber = "#111222333";
    String multiFactorAuthCode = "12345678";

    // Delete an MFA-protected object version
    restS3Service.deleteVersionedObjectWithMFA(versionId,
        multiFactorSerialNumber, multiFactorAuthCode,
        "bucket-name", "object-name");

The addition of MFA support at the API level in S3 is particularly
interesting because this is the first time Amazon has done so, and
because it raises some interesting challenges for developers who are
accustomed to building fully-automated systems. To take advantage of the
protection the MFA provides a system will need to prompt the user for
her MFA code every 30 seconds or so when she wishes to permanently
delete data. I am keen to see how -- and if -- developers actually build
this feature into their applications.

### Hello BitBucket

Finally, repeating the news I [posted recently][] on the JetS3t
discussion forums, I have decided to move the JetS3t codebase from it's
old home at java.net over to the BitBucket service:
<http://bitbucket.org/jmurty/jets3t/>

BitBucket has the advantage of being a more modern, easy-to-navigate
site, and has seamless support for Mercurial which is my favorite source
code management tool. So it's farewell to java.net and CVS, you served
us well but it's time for some new blood.

Try out the latest code and let me know what you think. Head over to the
[JetS3t BitBucket][] repository and grab the latest code via a pull (if
you're familiar with Mercurial) or simply download it via the "get
source" link.

  [beta versioning]: http://james.murty.co/2010/01/20/jets3t-s3-versioning/
  [now available in all regions]: http://aws.typepad.com/aws/2010/02/amazon-s3-enhancement-versioning.html
  [purchased one of these devices]: http://aws.amazon.com/mfa/
  [AWS Console]: http://aws.amazon.com/console/
  [posted recently]: http://groups.google.com/group/jets3t-users/browse_thread/thread/63dd1962b77e08f7?hl=en
  [JetS3t BitBucket]: http://bitbucket.org/jmurty/jets3t/
