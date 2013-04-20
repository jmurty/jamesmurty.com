Title: Shell script to find a class in a set of Jar files
Date: 2008-02-19 16:01
Author: James
Tags: Coding
Slug: find-class-in-jar

When you work on a Java project with many library dependencies it can be
difficult to know which Jar files contain which classes. Hunting down a
particular class in a tangled mess of Jar files can be painful,
especially if you need to do so on a server over a shell connection.

Here is a handy shell script that iterates over all the Jar archives in
a given path, finds those containing file names that match a given
pattern, and prints out these matches followed by the name of the Jar
file.

    :::bash
    #!/bin/sh

    if [ -z "$2" ]
    then
      echo Usage: $0 Directory ClassName
      exit 1
    fi

    for f in $(find $1 -name '*.jar')
    do
      jar tf $f | grep "$2" && echo "[in $f]"
    done

Save this script to a file with an obvious name, like *findInJars.sh*.

To find all the classes with names containing "HttpClient" in the *libs*
directory, you would invoke the script like so:

    :::console
    $ sh findInJars.sh libs HttpClient

    org/apache/commons/httpclient/HttpClient.class
    org/apache/commons/httpclient/HttpClientError.class
    org/apache/commons/httpclient/params/HttpClientParams.class
    [in libs/commons-httpclient/commons-httpclient-3.1.jar]

If you are impatient, you can accomplish the same thing with a big and
ugly one-liner:

    :::console
    for f in $(find libs -name '*.jar'); do jar tf $f | grep HttpClient && echo "[in $f]"; done

