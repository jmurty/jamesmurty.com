Title: SimpleDB Now Open to the Public, with Improvements
Date: 2008-12-02 08:16
Author: James
Tags: AWS
Slug: simpledb-open-to-the-public

Amazon's [SimpleDB][] online data storage and querying service is [now
in unlimited public beta][], which means that you can sign up for the
service and have your account activated immediately. Previously, new
users had to wait an indeterminate amount of time until they were
granted access to the limited beta.

Amazon has also changed the service's [pricing][] to encourage people to
try the service and stick with it. Moderate usage of the service will be
**free** for at least six months for up to 1GB of data, while the
ongoing data storage costs beyond 1GB have been slashed from $1.50 to
$0.25 per GB/month.

Finally, a new DomainMetadata API operation will be made available for
retrieving statistics about a domain ("database" in SimpleDB parlance)
such as the total number of items, and the storage consumed by all of
your attribute names and values. ~~Unfortunately the link to the
[DomainMetadata API documentation][] link is broken as I write this, but
full details are available in the [PDF version of the Developer
Guide][].~~ The DomainMetadata API documentation is now available in
both [HTML][DomainMetadata API documentation] and [PDF][PDF version of
the Developer Guide] versions of the Developer Guide.

  [SimpleDB]: http://aws.amazon.com/simpledb/
  [now in unlimited public beta]: http://aws.typepad.com/aws/2008/11/amazon-simpledb-grows-up.html
  [pricing]: http://aws.amazon.com/simpledb/#pricing
  [DomainMetadata API documentation]: http://docs.amazonwebservices.com/AmazonSimpleDB/2007-11-07/DeveloperGuide/SDB_API_DomainMetadata.html
  [PDF version of the Developer Guide]: http://s3.amazonaws.com/awsdocs/SDB/2007-11-07/sdb-dg-2007-11-07.pdf
