Title: AWS Security Update: Signature Version 2 for AWS Query APIs
Date: 2008-12-31 15:54
Author: James
Tags: AWS
Slug: aws-query-signature-version-2

Amazon has announced an improved request signature protocol for
authenticating HTTP requests sent to SimpleDB, to Elastic Compute Cloud
(EC2), or to the Simple Queue Service (SQS). The new protocol, version
2, fixes a security flaw in the version 1 signature algorithm.

The security flaw was identified by Colin Percival, who describes it in
detail in his article [AWS signature version 1 is insecure][]. As he
says:

> If you are making Query (aka REST) requests to Amazon SimpleDB, to
> Amazon Elastic Compute Cloud (EC2), or to Amazon Simple Queue Service
> (SQS) over HTTP, and there is any way for an attacker to provide you
> with data which you use to construct your request, switch to HTTPS or
> start using AWS signature version 2 now.

The good news is that your application will not be vulnerable to this
problem if it meets any of these conditions:

-   Sends requests securely using HTTPS
-   Does not include any user-provided data in its request parameters
-   Uses the SOAP API interface, instead of the Query (REST) interface

Regardless of whether or not your application is currently vulnerable,
if it uses the Query API interfaces you should start updating your
libraries or code immediately to use the version 2 signature because
**the old version will be phased out by October 2009**. While you are
thinking about security, Amazon has provided the article
[Making Secure Requests to Amazon Web Services][] which contains
recommendations for making secure requests to Amazon Web Services for all
interfaces.

If you need to adjust your application code to use version 2 signatures,
read on to see some example code.

In my book [Programming Amazon Web Services (O’Reilly 2008)][] I
demonstrate how to build clients that interact with Amazon's Query API
interfaces. Let's look at the ruby code for the AWS class that generates
version 1 signatures, and see how to adjust it to work with the new
version 2 protocol. (The book's sample code is available in Ruby, Python
and Java flavours from <http://examples.oreilly.com/9780596515812/>.
Jump to the end of this post to download the modified AWS class file).

#### Version 1 Query Signatures

It was very easy to generate the version 1 signature for AWS Query
requests. Give a hash map of request parameters, it was simply a matter
of sorting the parameters alphabetically (ignoring case) and merging
them into a string before applying the SHA encryption algorithm. Here is
the original signature generation code:

    :::ruby
    req_desc = parameters.sort {|x,y| x[0].downcase <=> y[0].downcase}.to_s
    signature = generate_signature(req_desc)

#### Version 2 Query Signatures

There are six key differences for generating version 2 signatures, most
(but not all...) of which are described in Amazon's documentation for
[authenticating SimpleDB REST requests][]:

-   The `SignatureVersion` parameter must have the value `2` (obviously)
-   Parameters are now sorted by "natural byte" ordering, which means
    you pay attention to the case of the parameter name when sorting
-   Parameter names and values must now be URL encoded. Be careful to
    ensure that space characters are encoded as `%20`, not `+`
-   When parameters are merged into a canonical string, they are now
    delimited by `=` and `&` characters as with a standard URL. For
    example: `Param1=SomeValue&Param2=AnotherValue`
-   The request description string to sign must include the HTTP method
    name (POST, GET etc), the target host name, and the target request
    path in addition to the canonicalized parameters string
-   Signatures can now be generated with either the original SHA 1
    encryption algorithm, or with the stronger SHA 256 algorithm. To
    indicate which algorithm you used, you must include the new
    `SignatureMethod` parameter with a value of `HmacSHA1` or
    `HmacSHA256`.

Here is some ruby code that follows these rules and generates a version
2 signature. It also takes advantage of the new support for the SHA 256
encryption algorithm:

    :::ruby
    # Use the strongest HMAC algorithm: SHA 256
    parameters['SignatureMethod'] = 'HmacSHA256'

    # Sort, and encode parameters into a canonical string.
    sorted_params = parameters.sort {|x,y| x[0] <=> y[0]}
    encoded_params = sorted_params.collect do |p|
      encoded = (CGI::escape(p[0].to_s) +
                 "=" + CGI::escape(p[1].to_s))
      # Ensure spaces are encoded as '%20', not '+'
      encoded.gsub('+', '%20')
    end
    params_string = encoded_params.join("&")

    # Generate the request description string
    req_desc =
      method + "\n" +
      uri.host.downcase + "\n" +
      uri.request_uri + "\n" +
      params_string

    # Generate the HMAC signature, using the SHA 256 digest
    signature = generate_signature(req_desc, digest='sha256')

For anyone following along with the original code, I also adjusted the
`generate_signature` method to accept an optional digest parameter that
specifies the encryption algorithm to use:

    :::ruby
    def generate_signature(request_description, digest='sha1')
      raise "aws_access_key is not set" if not @aws_access_key
      raise "aws_secret_key is not set" if not @aws_secret_key

      digest_generator = OpenSSL::Digest::Digest.new(digest)
      digest = OpenSSL::HMAC.digest(digest_generator,
                                    @aws_secret_key,
                                    request_description)
      b64_sig = encode_base64(digest)
      return b64_sig
    end

Of course, in addition to the ability to generate version 2 signatures,
the AWS class should retain the ability to generate version 1 signatures
if the client requests it. Download the final updated [AWS.rb][] class
file to see all the changes -- they are mostly in the `do_query` method.

  [AWS signature version 1 is insecure]: http://www.daemonology.net/blog/2008-12-18-AWS-signature-version-1-is-insecure.html
  [Making Secure Requests to Amazon Web Services]: http://developer.amazonwebservices.com/connect/entry.jspa?externalID=1928
  [Programming Amazon Web Services (O’Reilly 2008)]: http://www.amazon.com/gp/product/0596515812?ie=UTF8&tag=jamesmurty-20&linkCode=as2&camp=1789&creative=9325&creativeASIN=0596515812
  [authenticating SimpleDB REST requests]: http://docs.amazonwebservices.com/AmazonSimpleDB/latest/DeveloperGuide/REST_RESTAuth.html
  [AWS.rb]: http://james.murty.co/static/files/2008/12/aws.rb
