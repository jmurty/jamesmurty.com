Title: SOAP - the complexity of simple
Date: 2008-02-15 17:17
Author: James
Tags: Coding
Slug: soap-the-complexity-of-simple

A friend recently asked me how to go about writing code to access a SOAP
API to perform a one-off task.

Below is the bare-bones step-by-step summary I sent him. I feel sorry
for anyone encountering this travesty for the first time...

-   Find a good free SOAP library (eg Apache Axis)
-   Obtain the WSDL (Web Service Definition Language) document that
    describes the SOAP service you will talk to
-   Feed the WSDL into a tool in your SOAP library to generate client
    stub code. This stub code exposes the services functionality and
    handles all communication. Each SOAP library should have such a
    tool, but they all work differently
-   Write your program to use the client stub code. You will generally
    build up objects representing your data using classes provided in
    the client stub code, then call a "send" method of some sort to
    actually transmit that data to the SOAP service
-   Hope like crazy that the SOAP library you chose is compatible with
    the library used by the service. If not, start again at point 1

