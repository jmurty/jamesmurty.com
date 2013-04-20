Title: How to use JetS3t with Eucalyptus
Date: 2009-04-30 14:38
Author: James
Tags: Cloud Computing, Eucalyptus, JetS3t, Tips
Slug: how-to-use-jets3t-with-eucalyptus

**Updated 2009-06-22:** Added settings that limit JetS3t to a single
HTTP connection at a time, to work around apparent thread-safety issues
in Walrus.

[Eucalyptus][] is a relatively new but rapidly developing open-source
system for running your own cloud computing clusters. There have been
some exciting announcements recently around this project: it has been
added to Ubuntu 9.04 as the Ubuntu Enterprise Cloud technology preview,
integrated into [RightScale's cloud management service][], and has
received some venture funding.

What does all of this mean? It is becoming easier to create your own
cloud computing platform using open-source tools, and then to combine
your own cloud with public services like Amazon's AWS in interesting
ways.

As well as helping you manage your own cloud computing clusters,
Eucalyptus includes a storage service called [Walrus][] that is (almost)
interface compatible with Amazon's own S3 storage service. Great! So now
you can have your own personal S3-style storage service, but surely
there should be an easier way to interact with this storage than using
the `s3curl.pl` tool as described in the Walrus documentation?

Happily, the upcoming version of JetS3t will be compatible with the
Walrus. Goo goo ga joob.

#### Configuring JetS3t for Eucalyptus/Walrus

To use JetS3t with the Eucalyptus storage service you will need version
0.7.1 -- this probably won't be available on the [download page][] until
May 8th or so, but you can grab the pre-release code from the
[CVS repository][] and build it yourself if you are keen (a *java.net*
account is required).

Once you have the latest version, you will need to configure JetS3t to
talk to your own Walrus service by editing the `jets3t.properties` file
in the `configs` directory. In summary, you must tell JetS3t where your
Eucalyptus cluster service is located and turn off the HTTPS and
DNS-naming features that are not yet supported by Walrus.

Here are the non-default settings I used to talk to a Eucalyptus
front-end running on my own server with the IP address 192.168.1.128:

    :::properties
    s3service.s3-endpoint=192.168.1.128
    s3service.s3-endpoint-http-port=8773
    s3service.s3-endpoint-virtual-path=/services/Walrus

    s3service.https-only=false

    s3service.disable-dns-buckets=true

Depending on the version of Walrus you are using, you may need to apply
some additional settings. As of June 2009, there is [some evidence][]
that Walrus is not entirely thread-safe and will behave badly if you
perform multiple simultaneous requests. You can work around this issue
while still taking advantage of JetS3t's multi-threaded tools by
configuring JetS3t to use only one HTTP connection at a time:

    :::properties
    s3service.max-thread-count=1
    s3service.admin-max-thread-count=1
    httpclient.max-connections=1

With settings like these you should be able to interact with your
cluster's storage using the JetS3t API library or with the Cockpit
graphical tool.

![Cockpit accessing my Eucalyptus storage][]

To log in to your storage you will need to look up your *Query interface*
ID and secret key on the Credentials page of the Eucalyptus
web administration tool -- just hit the "Show keys" button. You will use
these credentials wherever you would normally use your Amazon AWS
credentials.

#### More Information

Here is a guide to [installing and configuring Eucalyptus on Ubuntu 9.04][].
It's not necessarily a straight-forward process and I got stuck on a couple of
steps myself, so I'm probably not the best person to ask if you run into
installation difficulties.

  [Eucalyptus]: http://www.eucalyptus.com/
  [RightScale's cloud management service]: http://blog.rightscale.com/2009/04/20/rightscale-ubuntu-eucalyptus-cloud-in-a-box/
  [Walrus]: http://open.eucalyptus.com/wiki/EucalyptusStorage_v1.4
  [download page]: http://jets3t.s3.amazonaws.com/downloads.html
  [CVS repository]: https://jets3t.dev.java.net/source/browse/jets3t/
  [some evidence]: http://groups.google.com/group/jets3t-users/browse_thread/thread/8b2c83a8bbba391e?hl=en
  [Cockpit accessing my Eucalyptus storage]: http://www.jamesmurty.com/wordpress/wp-content/uploads/2009/04/cockpit-to-eucalyptus-300x145.jpg
  [installing and configuring Eucalyptus on Ubuntu 9.04]: http://doc.ubuntu.com/ubuntu/serverguide/C/eucalyptus.html
