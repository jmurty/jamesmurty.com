Title: JetS3t Supports "Reduced Redundancy" Storage
Date: 2010-05-19 23:16
Author: James
Tags: JetS3t
Slug: jets3t-supports-reduced-redundancy-storage

As of a few minutes ago the latest JetS3t code includes support for a
new S3 feature called Reduced Redundancy Storage. If you keep non-vital
data in S3 you can now choose to accept "reduced redundancy" for this
data in return for a cheaper storage rate.

Accept a little more risk, save some bucks. For many S3 customers this
will be an attractive option.

See Amazon's [RRS blog post][] for more information.

Below is a brief overview of how you can use the feature in JetS3t once
you have [downloaded and built the latest code][].

### Cockpit

The Cockpit application has support for the new storage class in a few
places:

-   In the preferences you can choose the default storage class to apply
    when uploading objects
-   the Copy or Move Objects dialog allows you to choose the storage
    class for destination objects. This makes it easy to apply the
    cheaper storage option to many objects, you simply **copy** the
    objects in-place after selected the REDUCED\_REDUNDANCY storage
    class
-   each object's current storage class is now shown in the Object
    Attributes dialog.

### API

In the API you set the storage class of an object prior to uploading
it:

    :::java
    // Create an object as usual
    S3Object object = new S3Object("my-object", "some data");
    // Set the non-default storage class prior to upload
    object.setStorageClass(S3Object.STORAGE_CLASS_REDUCED_REDUNDANCY);
    // Upload as usual
    s3Service.putObject("bucket-name", object);

To apply the new storage class to existing objects you call the normal
RestS3Service copyObject or moveObject methods after setting the storage
class attribute of each destination object.

To check the storage class an object is stored under you perform a
bucket listing then call the S3Object's getStorageClass method:

    :::java
    S3Object[] objects = s3Service.listObjects("bucket-name");
    for (int i = 0; i < objects.length; i++) {
        System.out.println(objects[i].getKey()
            + ": " + objects[i].getStorageClass());
    }

  [RRS blog post]: http://aws.typepad.com/aws/2010/05/new-amazon-s3-reduced-redundancy-storage-rrs.html
  [downloaded and built the latest code]: http://bitbucket.org/jmurty/jets3t/wiki/Build_Instructions
