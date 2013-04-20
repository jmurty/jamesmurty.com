Title: Work-around for Mac OS X python package install error -- "lipo: can't figure out the architecture type"
Date: 2011-01-29 12:01
Author: James
Tags: Python, Tips
Slug: work-around-osx-lipo-figure-out-architecture-type

This is just some quick documentation of a couple of work-arounds I
needed to install the a python package on Mac OS X 10.6.6 (Snow
Leopard). This solution could work in a number of cases, not just for
this one package, so I thought I should write it down.

I was trying to install the [nose-cov][] unit test coverage package,
which depends on [coverage][], using the standard pip/easy\_install
commands without much luck. The compilation phase spat out a stream of
error lines followed by the final message: `failed with error code 1`.

### Mac OS X 10.4 Support

The first issue was that the coverage package required the optional "Mac
OS X 10.4 Support" component of XCode, as hinted at by this message I
found in the middle of the error log:

    :::text
    Compiling with an SDK that doesn't seem to exist: /Developer/SDKs/MacOSX10.4u.sdk
    Please check your Xcode installation

I did not have the 10.4 components installed on my 10.6 machine despite
having the rest of the (presumably 10.5+) components. This is easy to
fix by re-running the XCode installation from your OS X disk and
choosing the extra option.

### GCC Version 4.0 FTW

After installing the 10.4 pieces the installation still failed, this
time with the following message near the end of the error log:

    :::text
    lipo: can't figure out the architecture type of: /some/file

    error: command 'gcc' failed with exit status 1

#### [Edit: 2011-02-25]

A much cleaner way to make your system use GCC version 4.0 instead of a
later version is to use the `CC` environment variable. Prefix your
pip/easy\_install command with CC=/path/to/desired/gcc-version like so:

    :::bash
    CC=/usr/bin/gcc-4.0 pip install SOMETHING

**Try the CC environment variable approach above before you attempt the
hack below.**

Google lead me to [this post][] which provided the solution, though it
feels like a nasty hack.

My version of OS X (10.6.6) includes two versions of the gcc compiler
executable in /usr/bin:

    :::bash
    $ ls -al /usr/bin | grep gcc
    lrwxr-xr-x     1 root   wheel           7 29 Jan 10:01 cc -> gcc-4.2
    lrwxr-xr-x     1 root   wheel           7 29 Jan 10:01 gcc -> gcc-4.2
    -rwxr-xr-x     1 root   wheel       97392 18 May  2009 gcc-4.0
    -rwxr-xr-x     1 root   wheel      166128 18 May  2009 gcc-4.2
    . . .

The gcc symlink points to gcc-4.2 but only the gcc-4.0 version
successfully compiles the package. I **temporarily** moved the original
gcc symlink out of the way and created a new one pointing to the 4.0
version, like so:

    :::bash
    $ cd /usr/bin
    $ sudo mv gcc gcc_orig
    $ sudo ln -s gcc-4.0 gcc

I was then able to install the nose-cov package using pip and it ran
just fine. Great!

Finally I replaced the original symlink, because forgetting to do so
would almost certainly cause something else to break sooner or later:

    :::bash
    $ cd /usr/bin
    $ sudo rm gcc
    $ sudo mv gcc_orig gcc

So in the end my `/usr/bin` directory looks exactly the same as it used to
and the package is installed. Time to go do some real work.

  [nose-cov]: http://pypi.python.org/pypi/nose-cov/1.3
  [coverage]: http://pypi.python.org/pypi/coverage/3.4
  [this post]: http://www.mail-archive.com/rpy-list@lists.sourceforge.net/msg02672.html
