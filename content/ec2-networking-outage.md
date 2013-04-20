Title: EC2 Networking Outage
Date: 2008-04-08 11:37
Author: James
Tags: AWS
Slug: ec2-networking-outage

Amazon's Elastic Compute Cloud (EC2) service suffered a networking
outage yesterday that caused instances to become inaccessible from
outside Amazon's network. This meant that connections from the Internet
failed to reach some instances, though these instances continued running
and were accessible from other machines within EC2. The outage lasted
for up to an hour, according to comments in the discussion forums.

Amazon staff are investigating the issue and as of now there is no
official word on the cause, but what is likely to be of most interest to
EC2 users is whether all of the availability zones (locations) were
affected. If the outage was localized to one or two zones (out of three)
it would demonstrate the benefit of distributing your instances between
multiple zones using the new Availability Zone feature.

If all the zones were affected, this would demonstrate a central point
of failure that partially nullifies the strategy of distributing your
instances across zones. In this case, Amazon would need to modify the
architecture to remove the centralized failure point.

The [forum discussion thread][] contains conflicting reports from users
about whether the fault was localized or general. I will update this
post when more information is available.

#### Update

An Amazon staff member has posted a [post mortem comment][] stating that
this networking issue did indeed affect multiple Availability Zones. It
looks like this happened because the failure was caused by
misconfiguration rather than by a hardware or connection failure --
basically one of those completely unexpected events for which there are
no contingency plans.

This was an embarrassing glitch, and one which cannot be repeated if
developers are to believe that different availability zones give true
isolation from failures.

On the bright side, the issue was fixed quickly despite the cause being
difficult to find, and the full and frank explanation from Amazon gives
grounds for hope that the necessary monitoring and process improvements
will be put in place to prevent a repeat.

  [forum discussion thread]: http://developer.amazonwebservices.com/connect/thread.jspa?threadID=20932
  [post mortem comment]: http://developer.amazonwebservices.com/connect/thread.jspa?threadID=20932&messageID=85910#85910
