Title: IPython with Python version 2.6 on OS X Leopard
Date: 2009-06-05 22:09
Author: James
Tags: Python, Tips
Slug: ipython-with-python-2_6-osx-leopard

I recently installed the excellent [IPython][] program, a beefed-up
[Python][] console that provides a raft of extra features over the
default interpreter and makes it even more of a pleasure to work with
this language.

When you install IPython on Mac OS X Leopard using the standard method,
it only installs against the system's default version of Python: 2.5.1.
However, since I had previously installed Python version 2.6.1 on my
system I wanted IPython to work with this newer release.

It was surprisingly difficult to find out how to achieve this, so in
case anyone else wishes to do the same here's the process that worked
for me. Download the IPython tarball from the [distributions][]
directory (e.g. `ipython-0.9.1.tar.gz`), extract the archive, change into
the extracted directory and run:

    :::bash
    sudo python2.6 setup.py install

Notice that the command explicitly invokes the 2.6 version of python
with the `python2.6` alias: this simple step is enough to
properly link your IPython installation with the newer Python. It is
obvious in hindsight that this would work, but I wasted enough time
pointlessly messing with environment variables and paths that I thought
it was worth a blog post.

Don't try this with the bleeding-edge Python 3K because IPython is not
yet compatible with this version, but it seems to work fine with 2.6.1.

  [IPython]: http://ipython.scipy.org/moin/
  [Python]: http://www.python.org/
  [distributions]: http://ipython.scipy.org/dist/
