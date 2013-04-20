Title: SimpleDB: Finally Supports Sorting
Date: 2008-07-30 00:36
Author: James
Tags: AWS, Coding
Slug: simpledb-sorting

The [latest version][] of Amazon's SimpleDB service is available, and
happily it now allows for sorting of query results. This
highly-anticipated feature will make the service much more useful.

Sorting still suffers from some [limitations][]: you can only sort by a
single attribute, you cannot perform sorting in queries that contain
`union` or `not` predicates, and the attribute against which you are
sorting must be present in a query predicate. However, it is still a
massive improvement on sorting query results in your own client code.

For example, given the following SimpleDB query that finds historic
stock records for a given time period:

    :::text
    ['Code' = 'AAPL'] intersection ['Date' > '2007-12-01']

With the new `sort` operator, you can now instruct the service to return
the results in reverse (descending) date order like so:

    :::text
    ['Code' = 'AAPL'] intersection ['Date' > '2007-12-01'] sort 'Date' desc

Although you can only sort by an attribute that is also mentioned in a
predicate, you can easily work around this restriction by including a
`starts-with ''` predicate for that criteria, which will always evaluate
to true. Here is a query to return stock records sorted according to the
closing price, from lowest to highest:

    :::text
    ['Code' = 'AAPL'] intersection ['Close' starts-with ''] sort 'Close' asc

The SimpleDB update also includes some other new features, such as a new
`does-not-start-with` operator and support for 10 predicates per query
instead of 5, but I think it is the sorting that will have the most
impact.

  [latest version]: http://developer.amazonwebservices.com/connect/entry.jspa?externalID=1637
  [limitations]: http://docs.amazonwebservices.com/AmazonSimpleDB/2007-11-07/DeveloperGuide/index.html?SortingData.html
