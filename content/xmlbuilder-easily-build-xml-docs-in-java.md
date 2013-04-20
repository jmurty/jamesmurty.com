Title: XMLBuilder : Easily build XML documents in Java
Date: 2008-12-14 17:34
Author: James
Tags: Coding, Java
Slug: xmlbuilder-easily-build-xml-docs-in-java

I have long been irked by the difficulty of creating simple XML
documents in Java code. While Java has excellent support for handling
XML in general, if you just need to whip up a quick document -- say, to
interact with a web service API -- you can quickly get lost in a messy
quagmire of JAXP code that is difficult to write, to debug, and to
stomach.

In the past, I have often resorted to building small XML documents using
string concatenation to avoid this headache. And I've felt ashamed every
time. Well, no more!

The [XMLBuilder][] project I have just made available via Google Code
contains a single utility class that makes it simple to create XML
documents using relatively sparse Java code.

To create this XML document:

    :::xml
    <?xml version="1.0" encoding="UTF-8"?>
    <projects>
        <java-xmlbuilder language="Java" scm="SVN">
            <location type="URL">
                http://code.google.com/p/java-xmlbuilder/
            </location>
        </java-xmlbuilder>
        <jetS3t language="Java" scm="CVS">
            <location type="URL">
                http://jets3t.s3.amazonaws.com/index.html
            </location>
        </jetS3t>
    </projects>

You would use the following code, which is nicely terse and closely
resembles the structure of the XML document it produces:

    :::java
    XMLBuilder builder = XMLBuilder.create("Projects")
        .e("java-xmlbuilder")
            .a("language", "Java")
            .a("scm","SVN")
            .e("Location")
                .a("type", "URL")
                .t("http://code.google.com/p/java-xmlbuilder/")
            .up()
        .up()
        .e("JetS3t")
            .a("language", "Java")
            .a("scm","CVS")
            .e("Location")
                .a("type", "URL")
                .t("http://jets3t.s3.amazonaws.com/index.html");

If you're interested, head on over the the Google Code project and
download a copy. Feedback is welcome.

  [XMLBuilder]: http://code.google.com/p/java-xmlbuilder/
