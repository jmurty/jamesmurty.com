Title: XCode 3.1 and SVN 1.5
Date: 2009-03-18 03:19
Author: James
Tags: Coding, Tips
Slug: xcode-31-and-svn-15

I am reading the book [Xcode 3 Unleashed][] to get to grips with Apple's
Xcode IDE.

While configuring a local Subversion code repository I came across a
couple of problems that had non-obvious solutions.

After creating an SVN repository in a local directory using the
`svnadmin create` command, Xcode 3.1 refused to recognise the repo and
complained about **Error: 180001**.

![Xcode 3 Error 180001][]

The "solution" to this first stumbling block was to accept the settings
anyway, then quit and restart Xcode itself (?!). After doing this, the
error message changed to an even more puzzling **Access Denied**.

![access-denied][]

This one had me stumped for a little while because all the file and
directory access permissions seemed OK. I was put onto the right track
by [Rastikan's post][] in the Apple Support forums. It turns out that
Xcode 3.1 is not compatible with Subversion versions after 1.4 whereas
my system has version 1.5.5.

Fortunately, it is possible to create backwards-compatible Subversion
repositories by providing the option `--pre-1.5-compatible` to the
`svnadmin` command like so:

    :::console
    svnadmin --pre-1.5-compatible create Example2

After creating a 1.4-compatible SVN repository with this command, Xcode
recognises it immediately and without a restart. Success!

Having finally gotten Xcode to recognise my SVN repository and after
investigating the relatively poor SCM tools and features built in to
Xcode, I realise it may actually be easier to manage everything with
Subversion's command line tools. Still, at least now I have the option.

  [Xcode 3 Unleashed]: http://www.amazon.com/gp/product/0321552636?ie=UTF8&tag=postpastjamem-20&linkCode=as2&camp=1789&creative=390957&creativeASIN=0321552636
  [Xcode 3 Error 180001]: http://james.murty.co/static/images/2009/03/error-180001.jpg "Xcode 3 Error 180001"
  [access-denied]: http://james.murty.co/static/images/2009/03/access-denied.jpg "access-denied"
  [Rastikan's post]: http://discussions.apple.com/message.jspa?messageID=9141013#9141013
