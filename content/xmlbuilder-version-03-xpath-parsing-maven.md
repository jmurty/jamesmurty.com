Title: XMLBuilder Version 0.3: XPath, Parsing and Maven Goodies
Date: 2009-06-11 12:22
Author: James
Tags: Coding, Java
Slug: xmlbuilder-version-03-xpath-parsing-maven

I have updated my small [java-xmlbuilder][] project with some nice new
features.

First, here's a reminder of what this project does:

> XML Builder is a utility that creates simple XML documents using
> relatively sparse Java code.
>
> It is intended to allow for quick and painless creation of XML
> documents where you might otherwise be tempted to use concatenated
> strings, and where you would rather not face the tedium and verbosity
> of coding with JAXP.

The new features include:

-   [Parse existing documents][] into an XMLBuilder object, so you can
    now easily add nodes to pre-existing documents.
-   [Use XPath queries][] to locate a specific element in your document.
    This is especially useful if you have parsed a document and you need
    to add new nodes at different locations in the DOM. Type in your
    XPath query and you can now jump directly to the right place.
-   The project now has a Maven-friendly structure, complete with a
    repository from which you can obtain the Jar file -- see the
    Downloads section on the project page for instructions. This great
    leap forwards is thanks to Dan Brown's instructions for
    [using Wagon to deploy Maven artifacts to Google's SVN][].
-   JUnit tests are now public in the repository, to help keep me
    honest.

People familiar with the project may notice that I have changed the
version numbering scheme. The latest version is 0.3, not 3. I think the
"0." prefix better indicates the maturity of this tool.

  [java-xmlbuilder]: http://code.google.com/p/java-xmlbuilder/
  [Parse existing documents]: http://code.google.com/p/java-xmlbuilder/wiki/ExampleUsage#Parse_XML
  [Use XPath queries]: http://code.google.com/p/java-xmlbuilder/wiki/ExampleUsage#Find_Nodes_with_XPath
  [using Wagon to deploy Maven artifacts to Google's SVN]: http://www.jroller.com/mrdon/entry/find_of_the_day_wagon
