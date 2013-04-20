Title: Elastra provides support for RDBMS in the cloud
Date: 2008-03-29 09:26
Author: James
Tags: AWS
Slug: elastra_cloud_server

ELASTRA recently announced their [ELASTRA Cloud Server][] product, a
server application that aims to make it significantly easier to design
and deploy cloud-based applications.

<!--more-->

The company is working to provide an application design and management
system that will allow users to:

-   specify their application’s components and architecture using a
    declarative mark-up language
-   deploy and manage the application in their chosen cloud service
    provider or virtual machine environment, and
-   monitor their application and scale it on demand.

At this stage, the server supports a number of open-source relational
database components that can be deployed to Amazon's EC2 and S3
services. This makes it possible to deploy a clustered, scalable RDBMS
to your EC2 instances where the data is automatically persisted to S3 to
survive any instance failures.

The product is currently only available to a limited set of users upon
application, however the company intends to make it generally available
in April. Pricing has not yet been announced, but it will be based on a
metered system where you pay according to your usage.

If the ELASTRA Cloud Server does indeed make it simple and economical to
run a highly-scalable and reliable RDBMS in EC2, it will be a huge boon
to developers who would rather spend their time building applications
than hand-crafting a database system to work well within the constraints
of Amazon's services.

  [ELASTRA Cloud Server]: http://www.elastra.com/products/elastra-cloud-server/
