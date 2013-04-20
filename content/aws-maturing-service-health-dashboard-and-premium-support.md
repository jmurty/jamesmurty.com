Title: AWS maturing: Service Health Dashboard and Premium Support
Date: 2008-04-18 11:15
Author: James
Tags: AWS
Slug: aws-maturing-service-health-dashboard-and-premium-support

Amazon has released two new support mechanisms for *Amazon Web Services*
(AWS) that will be very welcome to developers and businesses that rely
on these services. These announcements demonstrate that the AWS
environment is maturing rapidly as Amazon responds to feedback about
their services and addresses key weaknesses.  
<!--more-->

#### Service Health Dashboard

The Service Health Dashboard (<http://status.aws.amazon.com/>) is a web
site that displays the current and historical health status of the AWS
infrastructure services. This site will make it much easier to determine
whether any issues you experience are specific to your application or
network, or are related to a broader AWS fault.

The dashboard will replace the developer forums as the central place for
tracking service faults, and for receiving updates from the AWS team
about resolutions and work-arounds:

> ...we plan to use the Service Health Dashboard as the single place to
> update you about the onset of an issue, status, outlook, recovery, and
> post mortems.

Here is an example of feedback provided by the AWS team during an EC2
API issue:  
![Screenshot of Health Dashboard comments following a fault][]

An RSS feed is available for each service status category, so you don't
even need to visit the web site to be informed of status changes.

Importantly, the dashboard page also includes a [Report an Issue][] link
that provides a clear, unambiguous way to inform the AWS team of service
issues. This is a great improvement over having to post a message to the
developer forums, or send an email to the *webservices@amazon.com*
"technical enquiries" address.

![Report an Issue form][]

Unfortunately, you are required to log in to your AWS account before you
can report an issue. If there is a fault with the AWS log in
authentication mechanism, as there was [earlier this year][], it will be
difficult to submit a fault report.

There are more screenshots on the [AWS Blog][], or you can simply
[visit the site][] yourself to see.

#### AWS Premium Support

In addition to the health dashboard, Amazon has announced a new for-pay
technical support service called [AWS Premium Support][]. For businesses
running on Amazon's S3, EC2 or SQS infrastructure services, it promises
rapid, personalised support and on-demand technical assistance with the
ability to escalate issues to service specialists.

There are two levels of support, Silver and Gold. Both are provided on a
monthly contract basis with no long-term commitment. The Gold level
includes 24 x 7 x 365 support and telephone access, while the Silver
level provides U.S. business day support and access to a n online
ticketing system.

Pricing for premium support is based on a percentage of your monthly
service usage fees, with a minimum cost of $100 per month for Silver or
$400 per month for Gold. Refer to the [AWS Premium Support][] home page
and the [AWS blog][] for more information.

The prior AWS support mechanisms, including the developer forums, remain
free of charge.

  [Screenshot of Health Dashboard comments following a fault]: http://www.jamesmurty.com/wordpress/wp-content/uploads/2008/04/servicehealthdashboard-ec2-fault..png "Screenshot of Health Dashboard comments following a fault"
  [Report an Issue]: http://www.amazon.com/gp/html-forms-controller/aws-report-issue1
  [Report an Issue form]: http://www.jamesmurty.com/wordpress/wp-content/uploads/2008/04/servicehealthdashboard-report-issue-form.png "Report an Issue form"
  [earlier this year]: http://www.jamesmurty.com/2008/02/16/major-s3-and-aws-outage-leaves-us-in-the-dark-in-more-ways-than-one/
  [AWS Blog]: http://aws.typepad.com/aws/2008/04/the-service-hea.html
  [visit the site]: http://status.aws.amazon.com/
  [AWS Premium Support]: http://www.amazon.com/gp/browse.html?node=566801011
  [AWS blog]: http://aws.typepad.com/aws/2008/04/may-we-help-you.html
