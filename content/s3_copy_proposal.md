Title: Amazon is planning to add "copy" support to S3
Date: 2008-03-22 10:14
Author: James
Tags: AWS
Slug: s3_copy_proposal

Amazon AWS developers are planning to add a new "copy" feature to the
Simple Storage Service (S3) API that will make it possible to copy your
data objects to a new location in the service. This feature could be
used to rename objects you have already stored (copy to a new name), to
relocate them to a different bucket, or even to relocate them between S3
locations (US to EU, and vice versa).

At present, if you want to do any of these things you must upload all
the data from scratch and you cannot take advantage of the fact it is
already present in the service.

The feature proposal document is here:  
<http://doc.s3.amazonaws.com/proposals/copy.html>

And there is a forum discussion topic where you can ask further
questions and provide feedback on the proposal:  

[http://developer.amazonwebservices.com/connect/thread.jspa?threadID=20409][]

  [http://developer.amazonwebservices.com/connect/thread.jspa?threadID=20409]:
    http://developer.amazonwebservices.com/connect/thread.jspa?threadID=20409&tstart=0
