Title: Programming Amazon EC2 Version 2008-02-01
Date: 2008-04-29 17:42
Author: James
Tags: AWS, Coding, O'Reilly Book
Slug: programming-ec2-version-2008-02-01

Amazon has released an updated version of the Elastic Compute Cloud
(EC2) API with the version name `2008-02-01`. This release includes a
number of new features that were not available in the `2007-08-29`
version of the API that I discussed in the book
[Programming Amazon Web Services][] (PAWS). To help keep my readers
up-to-date with the capabilities of the EC2 service, this article contains a
description of the new features and demonstrates how to use them in code.

The `2008-02-01` EC2 API provides three important new features:

-   [User Selectable Kernels][] – Choose to run an alternative Linux
    kernel on your instance, in order to benefit from newer or
    differently-configured kernel versions.
-   [Availability Zones][] – Choose the locations in which your
    instances will run. You can distribute your instances across
    different locations for better fault tolerance, or concentrate them
    in a single location to minimize network latency and data transfer
    costs.
-   [Elastic IP Addresses][] – Reserve your own public IP addresses in
    the EC2 environment, and assign these addresses to your instances on
    demand. Elastic IPs allow you to make an instance accessible at a
    known public IP address, without the need to use a dynamic DNS
    service to simulate a static IP.

#### Getting Started {#gettingstarted}

The code examples in this article are based on an updated EC2 client
implementation that has been added to the sample code archive on the
[PAWS Examples][] web site. In this article I will use the Ruby
implementation, but the archive also includes equivalent implementations
in Java and Python.

Download the latest [PAWS_examples.zip][] archive file, unzip it, and
change to the *PAWS_examples/ruby* directory. This directory should
contain two EC2 clients:

    :::console
    $ cd PAWS_examples/ruby
    $ ls EC2*
    EC2.rb            EC2_2008-02-01.rb

The first file, *EC2.rb*, contains the original EC2 API implementation
from the PAWS book. The second file, *EC2_2008-02-01.rb*, contains new
and updated methods that work with the latest EC2 API version
`2008-02-01`. This is the EC2 client we will use in this article.

Start an interactive Ruby session with the *irb* command, and create a
client object from the latest EC2 API implementation:

    :::irb
    irb> require 'EC2_2008-02-01' # => true

    irb> ec2 = EC2.new('YourAwsAccessKey', 'YourAwsSecretKey')

To confirm that you are using the correct API version, use the
`describe_images` method to list the Amazon Machine Images (AMIs)
provided to the public by Amazon. The listing should include different
image types identified by the `:type` attribute. The image types should
include `machine`, `kernel` and `ramdisk` images. Some machine images
will also have `:kernel_id` and `:ramdisk_id` attributes.

Here is a portion of the results from a listing of Amazon’s images. The
first item is a kernel image, and the second is a machine image that
includes kernel and ramdisk identifier attributes:

    :::irb
    irb> require 'pp'  # => true

    irb> pp ec2.describe_images(:owners => 'amazon')
    [{:type=>"kernel",
      :is_public=>true,
      :architecture=>"x86_64",
      :owner_id=>"amazon",
      :state=>"available",
      :location=>
       "ec2-public-images/vmlinuz-2.6.18-xenU-ec2-v1.0.x86_64.aki.manifest.xml",
      :id=>"aki-9800e5f1"},
      . . .
     {:type=>"machine",
      :is_public=>true,
      :architecture=>"i386",
      :kernel_id=>"aki-a71cf9ce",
      :owner_id=>"amazon",
      :ramdisk_id=>"ari-a51cf9cc",
      :state=>"available",
      :location=>"ec2-public-images/fedora-8-i386-base-v1.06.manifest.xml",
      :id=>"ami-f51aff9c"},

The kernel and ramdisk image types are new additions to the EC2 API.
They make it possible to select an alternative Linux kernel.

#### User Selectable Kernels {#userselectablekernels}

The User Selectable Kernels feature allows you to choose to run an
alternative Linux kernel on your instances, in place of the default
kernel provided by Amazon. In prior versions of the EC2 API there was
only one kernel available for each instance type; a variation of the
Linux 2.6.16 Xen kernel. You can now choose from a collection of kernels
that have been made available by Amazon or Amazon-endorsed vendors.

With a range of kernels now available in EC2, it is easier to take
advantage of kernel improvements or alternative kernel configuration
settings that may benefit your application. Unfortunately, the range of
kernels is still limited to what Amazon and other vendors provide. You
cannot create your own customized kernel, though hopefully it will
become possible to do so in the future.

##### New Image Types: AKIs and ARIs join AMIs {#newimagetypes:akisandarisjoinamis}

Alternative kernels are made available in the EC2 environment as a new
type of image, known as an Amazon Kernel Image (AKI). Because some
kernels require additional drivers when they launch, there is another
new image type called an Amazon RAM disk Image (ARI) which stores driver
files. These two image types join the venerable Amazon Machine Image
(AMI) which has always been used in EC2 to store an instance’s root
volume.

On the [Amazon Machine Images][] page, you can see a listing of the
publicly available kernel, ramdisk, and machine images. This listing
contains links to pages with further information about the images. For
example, the page for a kernel image may describe the kernel’s
configuration, indicate whether it requires a ramdisk image, and include
links to module files that are compatible with the kernel. This
information can help you decide which kernel will work best with your
application.

You can also use the DescribeImages API operation to programmatically
list all the images that are available to you. The listing returned by
the service will include an attribute that describes the type of each
image, and you can also tell the type of an image from the beginning of
its identifier string which will be `ami-`, `aki-` or `ari-`.

Amazon machine images may be configured with default values for the
kernel and ramdisk that instances will use. If you list the attributes
for Amazon’s Fedora 8 public AMI (`ami-f51aff9c`), you can see that it
is associated with the kernel image `aki-a71cf9ce` and ramdisk image
`ari-a51cf9cc`:

    :::irb
    irb> pp ec2.describe_images(:image_ids => 'ami-f51aff9c')
    [{:type=>"machine",
      :location=>"ec2-public-images/fedora-8-i386-base-v1.06.manifest.xml",
      :is_public=>true,
      :owner_id=>"amazon",
      :architecture=>"i386",
      :kernel_id=>"aki-a71cf9ce",
      :state=>"available",
      :ramdisk_id=>"ari-a51cf9cc",
      :id=>"ami-f51aff9c"}]

##### Selecting Your Kernel {#selectingyourkernel}

To run your instance with an alternative kernel, you specify the
identifiers of your chosen kernel and ramdisk images when you perform
the RunInstances operation. Not all kernels require extra drivers, so
you will only need to include the ramdisk identifier when the kernel’s
description page indicates that the ramdisk is necessary.

You can select any of the available kernel images when you launch an
instance, however it is your responsibility to check that the kernel
will actually work with the AMI you are launching. EC2 will not prevent
you from using a kernel that is incompatible with the machine’s image or
the instance’s architecture, nor will it force you to use the correct
ramdisk image. Before you launch an instance with a non-standard kernel,
you should always double-check that it is compatible with your AMI.

To demonstrate how to select an alternative kernel, we will launch an
instance based on the Fedora 4 *Getting Started* machine image
(`ami-2bb65342`) that has been available for some time. However, we will
launch it with the new [2.6.18 Xen 3.1.0 kernel][] (`aki-9b00e5f2`)
instead of the default 2.6.16 version.

To launch the instance, invoke the `run_instances` method and provide a
`:kernel_id` option to specify the alternative kernel’s identifier.
Because this newer kernel does not require a ramdisk image, you will not
need to include the `:ramdisk_id` option.

    :::irb
    irb> reservation = ec2.run_instances('ami-2bb65342', 1, 1,
                          {:key_name => 'ec2-private-key',
                           :kernel_id => 'aki-9b00e5f2'})

Once the instance has entered the running state and has been assigned a
public DNS name…

    :::irb
    irb> pp ec2.describe_instances
    . . .
      :instances=>
       [{:public_dns=>"ec2-72-44-52-218.compute-1.amazonaws.com",
         :image_id=>"ami-2bb65342",
         :kernel_id=>"aki-9b00e5f2",
         :state=>"running",
         :id=>"i-fb1ad992",
         . . .

…log in to the instance using *ssh*, and confirm that it is indeed
running with the 2.6.18 Linux kernel.

    :::console
    $ ssh -i ec2-private-key.pem root@ec2-72-44-52-218.compute-1.amazonaws.com

    ec2# uname --kernel-release
    2.6.18-xenU-ec2-v1.0

On an instance, you can find out which kernel and ramdisk images it is
using by referring to the `kernel-id` and `ramdisk-id` metadata items:

    :::console
    ec2# curl -f http://169.254.169.254/2008-02-01/meta-data/kernel-id
    aki-9b00e5f2

If your instance is running with a non-standard kernel and ramdisk,
these metadata items will return the identifier values. If you did not
specify an alternative kernel or ramdisk, or if the instance was
launched using an earlier API version, these metadata items may return
404 errors. This is the case for the instance we just launched, which
does not have an associated ramdisk image:

    :::console
    ec2# curl -f http://169.254.169.254/2008-02-01/meta-data/ramdisk-id
    curl: (22) The requested URL returned error: 404

##### Modules for User Selected Kernels {#modulesforuserselectedkernels}

If you launch an instance with a non-standard kernel, it is likely that
the machine image will not include compatible kernel modules. If you
check the module files available by default on the *Getting Started*
AMI, you will see that they are not compatible with the new kernel you
are running:

    :::console
    ec2# ls /lib/modules
    2.6.16-1.2069_FC4  2.6.16-xenU  2.6.17-1.2142_FC4

To obtain kernel modules that are compatible with your chosen kernel,
you must either obtain pre-compiled module files, or compile them
yourself. Fortunately, the information page for the 2.6.18 kernel
includes a download link for compatible modules. To install these
modules, you can simply download an archive file and extract its
contents to the root of your instance’s file system:

    :::console
    ec2# wget http://ec2-downloads.s3.amazonaws.com/ec2-modules-2.6.18-xenU-ec2-v1.0-i686.tgz
    ec2# tar xzf ec2-modules-2.6.18-xenU-ec2-v1.0-i686.tgz -C /

    ec2# ls /lib/modules
    2.6.16-1.2069_FC4  2.6.16-xenU  2.6.17-1.2142_FC4  2.6.18-xenU-ec2-v1.0

    ec2# modprobe -l
    /lib/modules/2.6.18-xenU-ec2-v1.0/kernel/security/seclvl.ko
    /lib/modules/2.6.18-xenU-ec2-v1.0/kernel/security/commoncap.ko
    . . .

Pre-prepared module files are only available for some of the alternative
kernels. For the kernels without readily available modules, you should
check the EC2 developer forums to see if anyone has posted details on
where to find modules, or how to compile them.

##### Bundling AMIs to Use a Specific Kernel {#bundlingamistouseaspecifickernel}

When you use the latest version of the *ec2-bundle-vol* tool to create
your own AMI from a running instance, the tool will refer to the
instance’s metadata to discover which kernel and ramdisk images it is
using. The tool will then automatically apply these settings to the
bundled image it creates, which means that you can easily bundle a new
AMI from an instance without having to manually specify the kernel or
ramdisk identifiers.

If you wish to explicitly set the kernel and ramdisk identifiers, the
*ec2-bundle-vol* and *ec2-bundle-image* tools allow you to do so by
providing the `--kernel` and `--ramdisk` options. There are a few
situations where you may need to explicitly set these options:

-   If you are bundling an image created outside EC2, and you want the
    AMI to use an alternative kernel or ramdisk.
-   If you are bundling a running instance, but you want the resultant
    AMI to use a different kernel or ramdisk.
-   If you do not trust the *ec2-bundle-vol* tool to retrieve the
    instance’s settings from the metadata service.

#### Availability Zones {#availabilityzones}

The Availability Zones feature allows you to specify the location, or
locations, where your instances will be deployed and run by the EC2
environment. By controlling the placement of your instances, you can
easily disperse them across multiple EC2 locations for better fault
tolerance, or concentrate them in a single location to minimize network
latency and data transfer fees.

You can specify the location for your instances when you launch them, or
you can skip this step and allow EC2 to decide where to place your
instances based on the availability and health of each location. In
prior API versions, EC2 always chose the location for instances and
there was no way you could control, or query, their location.

##### EC2 Locations: Regions and Zones {#ec2locations:regionsandzones}

EC2 data center locations are described in terms of “regions” and
“availability zones”. A region is a broad expanse such as a country or
geographic area. At present there is only one EC2 region available, the
U.S. East Coast, so the `2008-02-01` API release does not provide a way
to specify alternative regional locations.

An availability zone is a smaller area than a region. Each availability
zone is a distinct location that is designed to be insulated from
failures in other zones, yet at the same time to have fast and cheap
network connectivity to other zones within the same region. In other
words, you can expect that instances running in one zone will be
insulated from network, power or disaster failures in another zone,
despite the fact that the zones are all located in the same region.

##### New Transfer Fees for Cross-Zone Data {#newtransferfeesforcross-zonedata}

With the release of the availability zones feature, Amazon updated the
pricing model for EC2 to add a fee for data transfers between instances
in different zones. From July 1st 2008, it will cost 1¢ per GB to
transfer data from an instance in one zone to instances in other zones.
Data transfer between instances in the same zone will be free, provided
you use the instances’ private IP addresses to communicate rather than
their public or Elastic IP addresses. Because many current EC2 users
have instances that were automatically distributed across multiple
availability zones by the prior EC2 API versions, Amazon has delayed
introducing this new fee until after June 30th 2008, to give users time
to relocate their instances and avoid the extra fees.

##### Zone Names {#zonenames}

The latest EC2 API version has a new operation,
DescribeAvailabilityZones, to list of the name and status of each EC2
availability zone. You can use the `describe_availability_zones` method
in the EC2 client to list these zones:

    :::irb
    irb> ec2.describe_availability_zones
    => [{:name=>"us-east-1a", :state=>"available"},
        {:name=>"us-east-1b", :state=>"available"},
        {:name=>"us-east-1c", :state=>"available"}]

The listing includes the name of each zone and its “state” (status),
which should generally be `available`. From the zone listing above, you
can see that there are currently three availability zones: `us-east-1a`,
`us-east-1b`, and `us-east-1c`.

These zone names are deliberately vague because the name of an
availability zone is not intended to identify a specific physical
location. On the contrary, the relationship between zone names and
actual physical locations is different for each EC2 user. In other
words, my `us-east-1a` location may be different from your `us-east-1a`
location.

If you run all of your instances in a single zone, they will be
physically near each other because that named zone is mapped to a single
specific location in your EC2 account. However, when other EC2 users run
instances within this zone name, their instances may or may not run in
the same physical location as yours, depending on whether their zone
name happens to map to the same physical location.

##### Launch an Instance in a Zone {#launchaninstanceinazone}

To run an instance in a specific availability zone, you must specify the
target zone name when you launch the instance. There is no way to
relocate an instance from one zone to another after it has been
launched. In the updated EC2 client, you can specify the availability
zone location where an instance will run by providing a `:zone` option
to the `run_instances` method.

Here is the command to launch an instance in a the `us-east-1a` zone:

    :::irb
    irb> ec2.run_instances('ami-2bb65342', 1, 1,
             {:key_name => 'ec2-private-key',
              :zone => 'us-east-1a'})

    => {:groups=>["default"],
     :owner_id=>"916472402845",
     :instances=>
      [{:type=>"m1.small",
        :public_dns=>nil,
        :reason=>nil,
        :index=>"0",
        :launch_time=>"2008-04-21T03:32:55.000Z",
        :key_name=>"ec2-private-key",
        :image_id=>"ami-2bb65342",
        :zone=>"us-east-1a",
        :state=>"pending",
        :id=>"i-4df73324",
        :private_dns=>nil}],
     :reservation_id=>"r-03a05c6a"}

In the EC2 service’s response to this method, the `:zone` attribute
indicates the availability zone location where the instance is running.
In the new API version, both the RunInstances and the DescribeInstances
API operations return an XML document with the element
`item/placement/availabilityZone` to describe the instance’s location.
You can also check which zone an instance is running in from the
instance itself, by referring to the `placement/availability-zone`
metadata item:

    :::console
    ec2# curl -f http://169.254.169.254/2008-02-01/meta-data/placement/availability-zone
    us-east-1a

#### Elastic IP Addresses {#elasticipaddresses}

The Elastic IP Addresses feature allows you to reserve your own public
IP addresses within EC2, and to programmatically associate these
addresses with your EC2 instances. An Elastic IP address can be assigned
to any of your instances, or reassigned from one instance to another,
within a matter of minutes. Once the address is associated with an
instance, you can access the instance via this public IP address and use
it as if it were a standard static IP.

With Elastic IP addresses, applications you run on EC2 instances benefit
from having a static IP address which allows for easy DNS mapping and
address-based filtering. You also gain the added benefit of being able
to reassign the address from one instance to another should an instance
fail, or need to be replaced.

In Chapter 7 of the book [Programming Amazon Web Services][], I
described how to use dynamic DNS services as a work-around for the lack
of static IP addresses in EC2. Now that EC2 includes the Elastic IP
feature, this work-around is no longer necessary.

The following new operations were added to the EC2 API to support
Elastic IPs. I will describe these operations in more detail below.

-   AllocateAddress - Reserve an Elastic IP address for your own use.
-   ReleaseAddress - Release a reserved address that you no longer need.
-   DescribeAddresses - List the addresses you have reserved, and the
    instance associated with each address (if any).
-   AssociateAddress - Assign an Elastic IP address to one of your
    instances.
-   DisassociateAddress - Remove the association between an Elastic IP
    address and an instance.

##### Reserve an Elastic IP {#reserveanelasticip}

To reserve an Elastic IP address for your own use, you need to allocate
an address to your EC2 account. Each address you allocate belongs to you
whether you are actively using it or not, and the address will remain
yours until you explicitly release it. To discourage hoarding of Elastic
IP addresses, Amazon imposes a limit of 5 addresses per account, though
you can request an increased limit. There is also a fee for Elastic IP
addresses that you have reserved but are not using: you will be charged
1¢ per hour for each address that is not associated with a running
instance. There is no charge for addresses that are associated with an
instance.

You can use the EC2 client’s `allocate_address` method to reserve an
Elastic IP address. This method returns the address that has been
allocated to your account:

    :::irb
    irb> ec2.allocate_address
    => "75.101.151.147"

You can list all of the addresses that you have allocated to your
account with the `describe_addresses` method:

    :::irb
    irb> ec2.describe_addresses
    => [{:public_ip=>"75.101.151.147", :instance_id=>nil}]

Because we have not yet associated our Elastic IP with an instance, the
`:instance_id` attribute in the last response has no value. Remember
that you will be charged 1¢ for each hour that you keep this address
without associating it with an instance.

##### Associate an Elastic IP with an Instance {#associateanelasticipwithaninstance}

To make an instance accessible via an Elastic IP, you associate the IP
address with the instance. When you associate an address with an
instance, the instance’s prior public IP address is replaced with the
elastic one. The address association process takes a few minutes, during
which time the instance will not be reachable from the Internet via the
old or new public addresses. Although the instance may not be publicly
visible, it will always remain accessible to other EC2 instances via its
private IP address, which never changes.

Here is a command that uses the `associate_address` method to assign the
`75.101.151.147` Elastic IP address to the instance `i-fb1ad992`.
Remember to close any *ssh* or other network connections to your
instance before you associate the address, as any existing connections
will break or behave strangely when the public address changes.

    :::irb
    irb> ec2.associate_address('i-fb1ad992', '75.101.151.147')
    => true

Now, when we list the Elastic IP addresses in our account, the listing
shows the instance that is associated with the address:

    :::irb
    irb> ec2.describe_addresses
    => [{:public_ip=>"75.101.151.147", :instance_id=>"i-fb1ad992"}]

When you associate an Elastic IP address with an instance, the EC2
service will run a process behind the scenes to remove the instance’s
original public IP address and replace it with your elastic address. It
may take a few seconds before the DescribeAddresses operation shows the
latest association between an address and an instance, and it could take
several minutes before the instance becomes accessible through its new
public address.

An instance can only ever have a single public IP address. When you
launch an instance, the EC2 environment automatically assigns it a
dynamic public IP address from a pool of addresses. If you associate an
Elastic IP address with an instance, the original dynamic address is
retired and returned to the pool when your Elastic IP takes its place.
If you disassociate an Elastic IP address from an instance, the instance
will be assigned a new dynamic address to take the place of the elastic
one, and your Elastic IP will no longer map to any of your instances. If
you terminate an instance that is associated with an Elastic IP address,
the service will disassociate the address before the instance is
terminated.

##### Reassign an Elastic IP between Instances {#reassignanelasticipbetweeninstances}

It is possible to reassign an Elastic IP address from one instance to
another, without manually disassociating the address from the original
instance. When you do this, the original instance will be assigned a
dynamic address, while the Elastic IP address will be assigned to the
target instance. The ability to reassign an Elastic IP provides a
powerful mechanism to redirect traffic from one instance to another
without changing the destination address used by clients.

You can reassign your Elastic IPs to any of your instances whenever you
wish, by simply associating the address with a new instance. If we were
to launch a new instance with the id `i-4df73324`, here is the command
that would reassign our Elastic IP address from the original
`i-fb1ad992` instance to the new `i-4df73324` instance:

    :::irb
    irb> ec2.associate_address('i-4df73324', '75.101.151.147')

Be careful though, because when you reassign an Elastic IP address in
this way, neither instance will be accessible from the Internet for a
number of minutes until the address association process is finished.

##### Disassociate and Delete Elastic IPs {#disassociateanddeleteelasticips}

To prevent traffic destined for an Elastic IP address from reaching any
of your instances, you can use the `disassociate_address` method to
remove the address from its original instance without reassigning it to
another one:

    :::irb
    irb> ec2.disassociate_address('i-4df73324', '75.101.151.147')

Within a few seconds of invoking this command, a listing of your
addresses will confirm that the association has been removed, although
it will take a few minutes for the whole disassociation process to
finish.

    :::irb
    irb> ec2.describe_addresses
    => [{:public_ip=>"75.101.151.147", :instance_id=>nil}]

If you no longer need an Elastic IP address, you should delete it from
your EC2 account to avoid paying the hourly unused-address fee. You
delete an address from your account using the `release_address` method.

    :::irb
    irb> ec2.release_address('75.101.151.147')

If you intend to use this address in the future you should *not* release
it, because there is no way to reclaim the same address later on. In
many cases, it may be worth keeping an infrequently-used Elastic IP
address, because the convenience of having a known IP address will
outweigh the cost. On the other hand, if you wish to be able to access
your instance via a known DNS name but you only run the instance
occasionally, you could use a dynamic DNS service as an alternative to
keeping an Elastic IP address.

#### Conclusion

The new features in the `2008-02-01` version of the EC2 API make the
service more flexible and powerful, giving you greater control over the
distribution, addressing, and configuration of your virtual machine
instances. Now it is time to think about how you can best take advantage
of these features in your own applications.

For more information about the latest EC2 API features, refer to
Amazon’s feature guides and API documentation:

-   [Feature Guide: User Selectable Kernels][]
-   [Feature Guide: EC2 Availability Zones][]
-   [Feature Guide: Elastic IP Addresses][]
-   [API Documentation: EC2 API Version 2008-02-01][]

  [Programming Amazon Web Services]: http://www.oreilly.com/catalog/9780596515812/
  [User Selectable Kernels]: #userselectablekernels "User Selectable Kernels"
  [Availability Zones]: #availabilityzones "Availability Zones"
  [Elastic IP Addresses]: #elasticipaddresses "Elastic IP Addresses"
  [PAWS Examples]: http://examples.oreilly.com/9780596515812/
  [PAWS_examples.zip]: http://examples.oreilly.com/9780596515812/PAWS_examples.zip
  [Amazon Machine Images]: http://developer.amazonwebservices.com/connect/kbcategory.jspa?categoryID=101
  [2.6.18 Xen 3.1.0 kernel]: http://developer.amazonwebservices.com/connect/entry.jspa?externalID=1350&categoryID=101
  [Feature Guide: User Selectable Kernels]: http://developer.amazonwebservices.com/connect/entry.jspa?externalID=1345&categoryID=100
  [Feature Guide: EC2 Availability Zones]: http://developer.amazonwebservices.com/connect/entry.jspa?externalID=1347&categoryID=100
  [Feature Guide: Elastic IP Addresses]: http://developer.amazonwebservices.com/connect/entry.jspa?externalID=1346&categoryID=100
  [API Documentation: EC2 API Version 2008-02-01]: http://docs.amazonwebservices.com/AWSEC2/2008-02-01/DeveloperGuide/
