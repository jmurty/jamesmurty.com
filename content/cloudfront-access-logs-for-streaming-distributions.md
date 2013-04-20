Title: CloudFront Access Logs for Streaming Distributions
Date: 2010-05-13 19:35
Author: James
Tags: JetS3t
Slug: cloudfront-access-logs-for-streaming-distributions

Amazon has [announced][] the new Access Logs feature for CloudFront
streaming distributions. With access logging turned on you can see when
and how people interact with your streamed content.

The latest JetS3t code provides basic API support for enabling and
managing these access logs, in much the same way as you do for
non-streaming distributions. See the recent [changes to the
CloudFrontSamples.java file][] for example usage.

Note that this new feature has not yet been widely tested so [file a bug
report][] to let me know if you have problems.

  [announced]: http://developer.amazonwebservices.com/connect/ann.jspa?annID=681
  [changes to the CloudFrontSamples.java file]: http://bitbucket.org/jmurty/jets3t/diff/src/org/jets3t/samples/CloudFrontSamples.java?diff2=1f37cf808f59&diff1=37f74a1201cb
  [file a bug report]: http://bitbucket.org/jmurty/jets3t/issues?status=new&status=open
