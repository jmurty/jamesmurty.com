Title: SSH Tip: Redirect External Internet Traffic to a Dev Machine
Date: 2008-07-20 18:22
Author: James
Tags: Coding, Tips
Slug: ssh-external-redirect

When developing a web site or application, you may sometimes need to
expose the development version running inside your network to the public
Internet. This can be necessary to test the communication between your
application and an external service, such as PayPal.

If you have secure shell access to a publicly accessible server, you
can achieve this using the port forwarding feature of *ssh* to redirect
traffic from the Internet to your own machine. Ideally, you would use
the secure shell's `-R` option to forward a remote port. For example, to
forward traffic arriving on port 8888 of your public server to port 8000
on your local machine you would do the following:

    :::console
    ssh -R *:8888:127.0.0.1:8000

However, for remote forwarding to work the **GatewayPorts** option must
be enabled on your public server. This option is rarely enabled by
default, and if you lack the admin privileges or desire to change this
setting you will be unable to use remote port forwarding directly.

In this situation there is a work-around that achieves the same result
without relying on the GatewayPorts setting being enabled: local port
forwarding *from* the public server back to your own machine. Because
your machine probably isn't accessible from the public server (at least,
it shouldn't be...) you will need to pre-prepare an ssh tunnel that will
allow you to connect back to your computer.

All this talk of tunnels upon tunnels is confusing, so let's cut
straight to the commands. First, log in to the public server with ssh
while opening a port to allow a reverse ssh connection back to your
machine. Here, I will forward the server's port 2222 to port 22 on my
local development machine:

    :::console
    ssh -R2222:127.0.0.1:22 james@publicserver.com

Now, connect back to your own computer using the tunnelled port 2222,
while at the same time opening a public port to direct Internet traffic
from the server to your machine. The following command will forward
traffic sent to the server's 8888 port back to my computer's 8000 port.

    :::console
    ssh -g -L8888:127.0.0.1:8000 -p 2222 jmurty@127.0.0.1

In this command, the `-g` option allows Internet traffic to be forwarded
from the server rather than just local traffic, and the name `jmurty` is
the user name credential for my development machine. Although I am
seemingly connecting to the server at the loopback address 127.0.0.1,
because I am using port 2222 I will actually be tunnelled back to the
machine I started from.

In my experience, this work-around will give you the desired results
even when the GatewayPorts setting is disabled on the server. It is not
an ideal solution because the tunnelled traffic is encrypted twice so it
is quite slow, but this trick may be useful as a stop-gap measure until
your server administrator enables this setting on the server.
