Title: Script to build a Java classpath
Date: 2008-05-13 11:52
Author: James
Tags: Coding, Tips
Slug: script-to-build-a-java-classpath

If you need to compile or run Java programs from the command line, it
can be a real hassle to identify all the jar libraries the program
requires and include them in your classpath.

Here is a short script that will do this work for you on Unix, Linux or
Mac systems. It finds all the jar files in the current directory or its
subdirectories, and merges the list into a classpath string delimited by
colon (`:`) characters.

    :::bash
    export CP=`find . -name '*.jar' | tr "\n" :`

You can then run your program like so:

    :::console
    java -classpath $CP MyProgram
