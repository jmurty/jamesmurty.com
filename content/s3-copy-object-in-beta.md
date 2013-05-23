Title: S3 Copy Object feature is now available in beta
Date: 2008-05-06 00:08
Author: James
Tags: AWS, Coding, JetS3t
Slug: s3-copy-object-in-beta

Amazon has [announced][] beta support for the Copy Object operation in
S3. This feature was pre-announced [in March][].

The copy functionality allows you to copy objects within or between your
S3 buckets, and optionally to replace the metadata associated with the
object in the process. The single new operation makes it possible to
copy, move, and rename your S3 objects, and you can even update an
object's metadata by copying the object in-place.  
<!--more-->  
The feature is only in beta release at this stage and you cannot yet
copy objects between the US and EU (Europe) locations.

I have added support for this operation to the JetS3t library toolkit,
so check out the latest version from CVS if you want to try it out.

For those using the example code from [Programming Amazon Web
Services][] (affiliate link), here is a method you can add to the S3
class in *S3.rb* to implement the copy feature:

    def copy_object(source_bucket_name, source_object_key,
      dest_bucket_name, dest_object_key, acl=nil, new_metadata=nil)

      headers = {}

      # Identify the source object
      headers['x-amz-copy-source'] = CGI::escape(
        source_bucket_name + '/' + source_object_key)

      # Copy metadata from original object, or replace the metadata.
      if new_metadata.nil?
        headers['x-amz-metadata-directive'] = 'COPY'
      else
        headers['x-amz-metadata-directive'] = 'REPLACE'
        headers.merge!(new_metadata)
      end

      # The Content-Length header must always be set.
      headers['Content-Length'] = '0'

      # Set the canned policy, may be: 'private', 'public-read',
      # 'public-read-write', 'authenticated-read'
      headers['x-amz-acl'] = acl if acl

      uri = generate_s3_uri(dest_bucket_name, dest_object_key)
      do_rest('PUT', uri, nil, headers)
      return true
    end

The following command uses the `copy_object` method to copy an object
named *Object.txt* from one bucket to another and make the resulting
object publicly-accessible:

    s3.copy_object('from-bucket', 'Object.txt',
      'to-bucket', 'Object.txt', 'public-read')

The following code will replace an object's metadata in-place without
creating a new object. This allows us to set new values for the content
type and "example-name" metadata items:

    metadata = {
      'Content-Type' => 'text/xml',
      'x-amz-meta-example-name' => 'Example Value'}

    s3.copy_object('from-bucket', 'Object.txt',
      'from-bucket', 'Object.txt', 'private', metadata)

  [announced]: http://developer.amazonwebservices.com/connect/thread.jspa?messageID=88304
  [in March]: http://jamesmurty.com/2008/03/22/s3_copy_proposal/
  [Programming Amazon Web Services]: http://www.amazon.com/gp/product/0596515812?ie=UTF8&tag=jamesmurty-20&link_code=as3&camp=211189&creative=373489&creativeASIN=0596515812
