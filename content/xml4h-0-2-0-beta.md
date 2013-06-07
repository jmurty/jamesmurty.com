Title: xml4h: XML for Humans in Python - Release 0.2.0
Date: 2013-06-07 12:00
Author: James
Tags: Coding, Python
Slug: xml4h-0-2-0

The latest release of [xml4h][gh], my Python XML processing library, is now
available.

Version 0.2.0 adds an adapter for the [(c)ElementTree][et] library versions
included with Python 2.7+, which means that fast XML processing and (very
basic) XPath support is now readily available without the need to install
the [lxml][] library.

Although, if you need to do anything serious with XML in Python you really
should still install [lxml][], believe me.

With this release I have shifted the project status from *alpha* to *beta*,
since the library is being used successfully in some real-world code and I'm
not planning to tweak the API too much more.

You can install *xml4h* from [PyPI][pypi] with *pip*, check out [the code][gh],
and read the [documentation][docs].

  [gh]: https://github.com/jmurty/xml4h
  [lxml]: http://lxml.de/
  [et]: http://docs.python.org/2/library/xml.etree.elementtree.html
  [docs]: https://xml4h.readthedocs.org
  [pypi]: http://pypi.python.org/pypi/xml4h
