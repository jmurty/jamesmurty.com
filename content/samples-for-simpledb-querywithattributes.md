Title: Code samples for new SimpleDB feature: QueryWithAttributes
Date: 2008-09-07 14:54
Author: James
Tags: AWS, Coding
Slug: samples-for-simpledb-querywithattributes

A [couple of weeks ago][], a new API operation was added to Amazon's
SimpleDB service: QueryWithAttributes. This operation makes it possible
to retrieve **all** the attribute data for SimpleDB items that match a
query. Previously, to retrieve item attributes it was necessary to
perform a Query request, then perform follow-up GetAttributes requests
for each result item returned by the service.

In this post, I will show how to extend the SimpleDB ruby client
implementation from my book [Programming Amazon Web Services][]
(O'Reilly 2008) to support this new operation, and give some usage
examples.  
<!--more-->  
Let's start by adding a new method `query_with_attributes` to the
SimpleDB Ruby sample code (available from
<http://examples.oreilly.com/9780596515812/>). Edit the file
*ruby/SimpleDB.rb* and add the following method definition after the
existing `query` method. If the code below looks wonky in your browser,
you can [download a file][] instead

    :::ruby
    def query_with_attributes(domain_name, query_expression=nil,
                              attribute_names=[], options={:fetch_all=>true})
      more_items = true
      next_token = nil
      items = []

      while more_items
        parameters = build_query_params(API_VERSION, SIGNATURE_VERSION,
          {
          'Action' => 'QueryWithAttributes',
          'DomainName' => domain_name,
          'QueryExpression' => query_expression,
          'MaxNumberOfItems' => options[:max_items],
          'NextToken' => next_token
          },{
          'AttributeName' => attribute_names,
          })

        xml_doc = do_sdb_query(parameters)

        xml_doc.elements.each('//Item') do |item_node|
          item = {'name' => item_node.elements['Name'].text}

          attributes = {}
          item_node.elements.each('Attribute') do |attribute_node|
            attr_name = attribute_node.elements['Name'].text
            value = attribute_node.elements['Value'].text

            if respond_to? :decode_attribute_value
              # Automatically decode attribute values if the method
              # decode_attribute_value is available in this class
              value = decode_attribute_value(value)
            end

            # An empty attribute value is an empty string, not nil.
            value = '' if value.nil?

            if attributes.has_key?(attr_name)
              attributes[attr_name] << value
            else
              attributes[attr_name] = [value]
            end
          end

          item['attributes'] = attributes
          items << item
        end

        if xml_doc.elements['//NextToken']
          next_token = xml_doc.elements['//NextToken'].text.gsub("\n","")
          more_items = options[:fetch_all]
        else
          more_items = false
        end
      end

      return items
    end

The `QueryWithAttributes` operation works almost exactly like the
SimpleDB service's `Query` operation, except it includes item attributes
in the result. You can optionally specify exactly which attributes to
retrieve using the `attributes` parameter, or leave this empty to
retrieve all item attributes.

Continuing on from the stock quote database example in my book, here is
the command you would issue to retrieve the records for days on which
more than 70 million Apple stocks were traded. Notice that I am taking
advantage of the new [sorting][] capabilities of SimpleDB to retrieve
ordered results:

    :::irb
    irb> query = "['Volume' > '#{sdb.encode_integer(70000000)}'] sort 'Volume'"
    irb> sdb = SimpleDB.new
    irb> sdb.query_with_attributes('stocks', query)
    => [{"name"=>"AAPL-2007-07-26T00:00:00Z",
      "attributes"=>

       {"Code"=>["AAPL"],
        "High"=>[148.5],
        "Open"=>[145.91],
        "Close"=>[146.0],
        "Date"=>[Thu Jul 26 00:00:00 UTC 2007],
        "Volume"=>[78093900],
        "Low"=>[136.96],
        "Adjusted Close"=>[146.0]}},
        . . .

If you were only interested in the Open and Close attribute values, you
could tell the service to include only these attributes in the results:

    :::irb
    irb> sdb.query_with_attributes('stocks', query, attributes=['Open','Close'])

It is a good idea to retrieve only the attributes you really need,
because the SimpleDB service limits each response message to 1 MB and
you will get more results in fewer requests if you reduce the amount of
data you are asking for.

The `QueryWithAttributes` operation makes it much easier to use SimpleDB
because you no longer need to perform follow-up queries to retrieve
attribute data. However, there may be a price to pay for this
convenience so be sure to run some tests before converting your
applications. It may turn out that, in some circumstances, you can
retrieve results more quickly using the Query/GetAttributes approach
with multiple request threads on your client, than you can using the
QueryWithAttributes operation.

In early [forum discussion][] it looks like the new operation is both
the easiest and fastest way to perform queries, but results may vary
depending on how you use the service, your dataset, and your network
performance.

If you are using SimpleDB with a large data set or complex queries, try
the new operation and discuss your experiences on the forum so we can
gain a better idea of the strengths and weaknesses (if any) of
QueryWithAttributes.

  [couple of weeks ago]: http://aws.typepad.com/aws/2008/08/amazon-simpledb.html
  [Programming Amazon Web Services]: http://www.amazon.com/gp/product/0596515812?ie=UTF8&tag=jamesmurty-20&linkCode=as2&camp=1789&creative=9325&creativeASIN=0596515812
  [download a file]: http://s3.jamesmurty.com/query_with_attributes.txt
  [sorting]: http://www.jamesmurty.com/2008/07/30/simpledb-sorting/
  [forum discussion]: http://developer.amazonwebservices.com/connect/thread.jspa?threadID=24190&tstart=0
