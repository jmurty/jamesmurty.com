Title: EC2 and SimpleDB News
Date: 2009-03-13 15:58
Author: James
Tags: AWS
Slug: ec2-and-simpledb-news

I have been out of blogging action for a little while due to an
international move. My first week in [Portland, OR, USA][] has been
great (though cold) and now that I have some time I should get back to
work...

#### EC2

**Reserved Instances**

The latest news regarding EC2 is the new [Reserved Instances][] feature.
This is a particularly interesting development of Amazon.com's "Pay as
you go" pricing model.

Reserved Instances is a mechanism that allows you to pre-pay for EC2
instances for a period of 1 or 3 years. When you pre-pay for (reserve)
instances, Amazon guarantees that these instances will be available when
you need them -- there is no risk that your request will exceed the
service's available instance pool.

Reserved instances also have a reduced hourly usage fee. The pricing is
structured such that if you run your instance most of the time, your
yearly costs will be less than for non-reserved instances. For example,
running a standard small instance 24/7 for 3 years costs about $2,628
(10¢ hourly x 24 hours x 365 days x 3 years) whereas a reserved instance
costs about $1,288 (3¢ hourly * 24 hours * 365 days * 3 years +
$500 one-time fee). That's a saving of over 50%, **if** you run your
instance full-time. See the [pricing][] topic in the EC2 FAQ for the
information you will need to run your own numbers.

It is important to note that aside from the guaranteed availability and
reduced fee for Reserved Instances, they work just like normal EC2
instances. You can start and stop them on demand, and (after the
one-time fee) you pay only for the time you run the instance.

Support for Reserved Instances is currently limited ~~to US EC2
locations (sorry Europe) and~~ to the Linux and OpenSolaris operating
systems (sorry Windows).

**Update:** Reserved instances are now available in Europe. The
reservation fees in the EU are the same as for US instances, but the
usage fees are slightly higher.

**Windows spreads on EC2**

To make up for the lack of Windows support with the new Reserved
Instances feature, here's some good news for our Microsoft-y readers.
You can now run Windows EC2 instances in more places: in
[two availability zones in Europe, and an extra two availability zones in the US][].

To go with the new support for running Windows in the EU region, there
are also some localised Windows AMIs with the French, German, Italian,
and Spanish language packs pre-installed. Follow the link in the prior
paragraph for more details.

**List of Public Data Sets keeps growing**

[Public Data Sets on AWS][] are repositories of publicly accessible data
that Amazon has made easily accessible to EC2 instances. Simply start an
EC2 instance, attach one of the pre-prepared Elastic Block Store disk
snapshots, and delve straight into the data.

There's lots of great stuff here, from Wikipedia (in English) to US
Census databases.

#### SimpleDB

**Select query language selected over query**

The [Select query language][], which provides a more SQL-like querying
language for SimpleDB, will completely replace the original
[Query language][] from around May 2010. The Query language is being
[deprecated over 15 months][] to allow Amazon to "focus ... future
development efforts on the Select API" which is preferred by many
SimpleDB users.

**Run long queries (over multiple requests)**

SimpleDB queries that run for longer than the 5 second cut-off no longer
terminate with an unhelpful timeout error. Instead, queries that exceed
this time will return any results found up until the cut-off point,
along with a token that you can pass back to the service to continue the
query for another 5 seconds.

**Count your results**

The SimpleDB Select API now supports a [count function][] that returns
the number of results found for a query, rather than the actual results.

#### That's it

Whew, what a list. Amazon has been almost as busy as I have over the
last few weeks.

  [Portland, OR, USA]: http://en.wikipedia.org/wiki/Portland,_Oregon
  [Reserved Instances]: http://aws.typepad.com/aws/2009/03/announcing-ec2-reserved-instances.html
  [pricing]: http://aws.amazon.com/ec2/faqs/#How_will_I_be_charged_and_billed_for_my_use_of_Amazon_EC2
  [two availability zones in Europe, and an extra two availability zones in the US]: http://aws.typepad.com/aws/2009/03/additional-windows-support-second-zone-in-the-us-and-2-zones-in-europe.html
  [Public Data Sets on AWS]: http://aws.amazon.com/publicdatasets/
  [Select query language]: http://docs.amazonwebservices.com/AmazonSimpleDB/latest/DeveloperGuide/UsingSelect.html
  [Query language]: http://docs.amazonwebservices.com/AmazonSimpleDB/latest/DeveloperGuide/UsingQuery.html
  [deprecated over 15 months]: http://developer.amazonwebservices.com/connect/ann.jspa?annID=409
  [count function]: http://docs.amazonwebservices.com/AmazonSimpleDB/latest/DeveloperGuide/CountingDataSelect.html
