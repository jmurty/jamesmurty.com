Title: SQS API update (2008-01-01)
Date: 2008-02-09 10:52
Author: James
Tags: AWS, O'Reilly Book
Slug: sqs-api-update-and-backwards-compatibility

Amazon have announced a new API version (2008-01-01) for the Simple
Queue Service. The new API promises much cheaper usage fees for the
service, but the API update includes a number of major changes that are
not compatible with prior API versions.

For those already familiar with SQS, you can find a detailed list of
changes in the document [Migrating to Amazon SQS API Version
2008-01-01][].

This new API works quite differently to the previous versions and will
not support all of the features necessary for the examples in the
Programming S3... book. In particular, the loss of the
`ChangeMessageVisibility` operation will make it impossible to implement
the automated visibility extension mechanism included in the boto
service example. The fact that all existing SQS tools will be
incompatible with the new API is also problematic for the SQS
Applications chapter.

The book is well into the production process and we will not have enough
time to update the SQS chapters to cover the new API, especially as we
would also have to wait until the third-party libraries and tools we
demonstrate to be updated. Keeping up with Amazon is proving to be quite
a challenge.

I will write sample code (Ruby, Java, Python) that is compatible with
the new API and will include this in the online resources we will make
available when the book is released. This code, and a brief summary of
API changes, may be as much as we can do to cover the new API in the
book.

  [Migrating to Amazon SQS API Version 2008-01-01]: http://developer.amazonwebservices.com/connect/entry.jspa?externalID=1148
