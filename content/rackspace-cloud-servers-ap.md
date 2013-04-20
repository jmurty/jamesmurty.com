Title: Rackspace Cloud Servers API
Date: 2009-07-14 10:28
Author: James
Tags: Cloud Computing
Slug: rackspace-cloud-servers-ap

Rackspace has [launched][] a public beta of their [Cloud Servers API][].

The Cloud Servers product allows you to rent computing resources and is
a competitor to Amazon's Elastic Compute Cloud (EC2) service. Rackspace
has a [comparison page][] that describes, from their perspective, the
advantages of their offering over EC2.

Some key differences from EC2 include:

-   Cloud Servers has a wider range of server sizes available at the low
    end, with a minimum size of 256MB RAM that has a price of only $10.95
    per month.
-   Public IP addresses can be shared among multiple servers.
-   The service supports dynamic resizing (vertical scaling) of servers
    to a degree. Unlike EC2, you can increase or decrease the computing
    power available to a single server without the need to manually
    start a new instance and redeploy your application to the new
    instance. However this scaling, while easy, isn't instantaneous --
    behind the scenes Rackspace's service actually starts a new server
    and copies everything across for you, so there is likely to be some
    downtime.
-   A simpler RESTful API with support for JSON messages in addition to
    XML.

I am not yet familiar enough with Cloud Servers to give a detailed
comparison with EC2, but it seems to be a full-featured service that is
aiming to address some of the difficulties people face when using
Amazon's offering. If Rackspace can learn from Amazon's missteps they
should be able to provide a compelling cloud computing platform.

It has taken some time for a strong, low-level "Infrastructure as a
Service" competitor to EC2 to arrive, but we may finally have it in
Cloud Servers. I hope so, because the more active competition we have in
this space the more quickly the products and technology will improve,
and the better off we cloud computing users will be.

  [launched]: http://blog.mosso.com/2009/07/an-interview-with-the-architects-of-the-cloud-servers-api/
  [Cloud Servers API]: http://www.rackspacecloud.com/cloud_hosting_products/servers/api
  [comparison page]: http://www.rackspacecloud.com/cloud_hosting_products/servers/compare
