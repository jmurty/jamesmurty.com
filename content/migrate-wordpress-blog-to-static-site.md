Title: How I Migrated my Wordpress Blog to a Static Site
Date: 2013-05-23 12:00
Author: James
Tags: Python
Slug: migrate-wordpress-blog-to-static-site


I have just finished  migrating my long-neglected blog from a self-hosted
Wordpress installation on my own VPS to a static site hosted on the
[Amazon S3][s3] storage service using its [website hosting][s3-website]
feature.

This post captures the main steps involved, in case anyone else is interested
in doing the same thing.

### Why Migrate from Wordpress?

My blog has run well enough on a self-hosted Wordpress set-up for years, first
at a cheap site hosting company (where performance was terrible) then on my own
[Linode][linode] VPS server (where performance has been great).

However, I have never been very happy relying on the PHP-based Wordpress
app due to the frequent security updates it requires and my gut-level distrust
of PHP itself. I know it well enough not to trust it, especially when my blog
can lie neglected for months at a time when I'm busy. It made me nervous
knowing I could be one tardy security-update away from a hacked site and
server.

Besides, this blog is small enough that any powerful blogging system is
overkill for my needs.

### Static Site Generation

Because my blog is simple, it is a perfect candidate to be served as a static
site instead of a dynamically-generated one. Instead of Wordpress and PHP code
running on my server to generate HTML pages when someone lands on a page, why
not just serve HTML pages directly? This is about as simple as it can get.

But even a simple blog like this is far too complex to hand-code all the HTML
and other files necessary to show do things like display a post, list all
posts, provide RSS/Atom syndication feeds for blog reader software, provide
sitemap XML files for Google, etc. etc. So I need a middle ground: a
[static site generator][].

At this stage it's worth saying explicitly that using static site generators,
while "simpler" from a web-server point of view, requires much more knowledge
about how web sites work and how to host them. As the rest of this post will
make clear, generating and hosting your own static site is an involved and
deeply nerdy process best suited to people who are web programmers, or
interested in becoming one.

#### Pelican

There are roughly fourteen bazillion site generator projects around, with the
number growing constantly.

I chose [Pelican][pelican] for my blog because:

 - It seems relatively well-established and mature in the field.
 - It allows posts to be written in Markdown (or other human-friendly markup
   languages)
 - It's written in Python, a language I like and that I can easily hack on if
   I want to contribute fixes or [improvements][pelican-pages-import] to the
   project.
 - It has plugins that do things like generating sitemap files and
   other niceties that would be tedious to build myself.

I installed a very recent code version (pre 3.3) of Pelican into a pre-prepared
[virtualenv][] Python environment. I used the latest code because it has
improvements that are particularly useful for migrating existing Wordpress
sites. I also installed some additional requirements:

    :::bash
    # Pelican pre 3.3 code version, with slug and pages import improvements
    pip install -e git+git@github.com:jmurty/pelican.git@675d6c81#egg=pelican-dev

    # Markdown for migrating and authoring posts in this markup language
    pip install Markdown==2.3.1

    # BeautifulSoup is required to migrate Wordpress posts
    pip install BeautifulSoup

After installation I ran the `pelican-quickstart` command to create initial
configuration files and some helper scripts.

Be warned though: the generated scripts have their own copies of configuration
settings you choose while running the quickstart, so if you subsequently change
your Pelican configuration files and run these scripts your config changes
will have no effect. I found this annoying enough that I ended up removing the
helper scripts and use the explicit Pelican commands instead.

### Migrate Data from Wordpress

#### Migrate Your Posts

Migrating my existing Wordpress blog posts was only somewhat difficult and
fiddly, to be honest it was easier than I expected:

 1. Manually install the additional
    [Pandoc universal document converter][pandoc] tool per the
    [Pelican Import][pelican-import-dependencies] documentation.
 2. [Export][wordpress-export] and download your Wordpress posts and comments
    as an XML file. I saved this file as `site.wordpress.xml`
 3. Run the `pelican-import` command to convert the Wordpress posts into
    Markdown-formatted files written to the `content` directory:

        :::bash
        pelican-import --wpfile --dir-page \
            --output content -markup markdown \
            site.wordpress.xml

At this stage you will hopefully have a collection of Markdown files that
correspond very closely to your Wordpress posts. Take a look at some of the
files and note the metadata included at the top; fields like `Title` and
`Slug` capture important information about the original posts.

Unfortunately I found the conversion process was imperfect so I needed to look
closely at many of the post files to check for quirks and then fix these issues
across all posts.

I also decided to use Tag instead of Category groupings for my posts, which
I should have done from the very beginning in Wordpress, but changing this was
straight-forward with some global find-and-replace changes in the markdown
files.

#### Migrate Your Comments

One drawback of static sites is that there is no way to do server-side
processing of comments submitted by site visitors. At least, not without
defeating the point of making your site static in the first place.

If you wish to allow comments on your static site you will need to use
a javascript-based commenting system, such as the one provided by
[Disqus][disqus].

I am using Disqus on the now-static site, as you will see if you view or leave
comments below. It was quite easy to set this up: I created an account on
the service, added my site details, and set the `DISQUS_SITENAME` setting in
Pelican's `publishconf.py` configuration file.

Because I also wanted to keep the comments from my existing Wordpress blog site
I also exported these comments by:

 - installing the *Disqus Comment System* plugin on my Wordpress site.
 - configuring my new Disqus site account in the plugin
 - exporting the comments from Wordpress to Disqus via the *Export Comments*
   button.
 - monitoring progress of the export on the Disqus dashboard.

The export process took a long time (days) and a few of my blog's comments
didn't survive the process, which isn't a big deal for my site but might be a
problem for others. Hopefully you will have better luck with this.

### Generate the Static Site HTML

Now that your content is in place you can generate a static site to check how
it all looks. Here is the command to convert the markdown files in `content/`
to static files to the `html/` directory:

    :::bash
    # Add --debug flag to see exactly what is happening
    pelican content/ -o html -s pelicanconf.py --delete-output-directory

You can now look directly at the generated files in the `html/` directory, or
run Pelican in server mode so you can view your blog in a web browser at
[http://localhost:8000/][localhost-8000] using the `develop_server.sh` helper
script generated by the "quickstart" process, or with the following explicit
commands:

    :::bash
    # Run Python's built-in web server on html/ as a background job
    cd html/
    python -m SimpleHTTPServer &

#### Customise the Generated Site Layout

Once you can view the generated site in a browser you can customise a number of
things in your `pelicanconf.py` configuration file to make the site work
exactly the way you want.

In my case I wanted the new static site to replace the original Wordpress one
without breaking all the links, because [Cool URIs don't change][cool-uris].
To do this I configured Pelican very carefully to generate URL paths matching
the datestamp + slug format I used in Wordpress, for example:

    :::python
    # Post/Article URL links have clean paths with date stamp + slug ...
    ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}/'
    # ... while the file is index.html to be auto-served from the dir location
    ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

I also customised where RSS/Atom feeds are saved, whether pages are displayed,
and other things. Check out the Pelican documentation to see what you can do.

#### Theme {#theme}

I created my own theme for the blog. You can tell because it's very simple, and
very ugly (I'm no designer).

It was pretty easy to do this by following the Pelican theming documentation
and stealing ideas and code snippets from the example themes available in
[Pelican Themes][pelican-themes] Github repository.

One particularly cool thing I will mention is how to use the excellent
[Solarized][solarized] colour themes for code snippets, so at least that part
of my blog isn't ugly. Generate the necessary CSS files like so:

    :::bash
    # Install Pygments and solarized style
    pip install Pygments pygments-style-solarized

    # Generate CSS files of light and dark solarized colours
    pygmentize -S solarizeddark -f html > solarizeddark.css
    pygmentize -S solarizedlight -f html > solarizedlight.css

You can then add these CSS files to your template to get solarized code
highlighting in your posts.

Note: I found I had to set the overall background colour to get things to
look right, here's what I did:

    :::css
    /* Add this line to the top of solarizedlight.css */
    pre { background: #fdf6e3; }

    /* Add this line to the top of solarizeddark.css */
    pre { background: #002b36 }

#### Pelican Plugins

The final Pelican-related tweaks I made were to add some existing plugins to do
useful work like generate a `sitemap.xml` file and make extra information
available to help with site navigation, such as lists of next/previous and
related posts.

To use the plugins I added the [pelican-plugins][pelican-plugins] codebase to
my project directory:

    :::bash
    git submodule add https://github.com/getpelican/pelican-plugins
    git submodule update --init

Then configured Pelican to find and use the relevant plugins:

    :::python
    PLUGIN_PATH = 'pelican-plugins'
    PLUGINS = ['sitemap', 'neighbors', 'related_posts']

    SITEMAP = {
        'format': 'xml',
        'changefreqs': {
                'pages': 'daily',
        }
    }

### Site Hosting with Amazon S3 in Website Hosting Mode

With a static blog site instead of a dynamic one, it was no longer necessary to
host it on my VPS server. By moving the site entirely to a static-file-serving
platform I could free up my VPS to the testing-ground I had originally
intended.

With it's relatively recently-added support for [website hosting][s3-website],
the Amazon S3 storage service made an attractive choice. It's pretty simple,
extremely reliable, fairly priced, and I'm very familiar with it.

The process for setting this up was made a bit complex because I had some extra
requirements:

 - My blog should be accessible at both the [jamesmurty.com][blog] root domain
   and the [www.jamesmurty.com][blog-subdomain] subdomain.
 - The old RSS feed endpoint at *http://www.jamesmurty.com/feed/* shouldn't
   change, so that subscribers continue receiving my blog posts (like this
   one).

To serve the site from S3 I needed to generate the site in a publishable form,
set up my S3 account to store and serve it, and tweak my domain's DNS
management to hook everything up correctly.

#### Generate Site for Publishing

By default the Pelican quickstart process produces two configuration files,
`pelicanconf.py` and `publishconf.py`. The former stores most of your settings
and is intended for use when developing or testing your site, while the latter
contains settings useful only for the published site.

In my case the `publishconf.py` file has two extra settings:

 - Relative URLs are disabled, to ensure in-post links work properly when read
   in an RSS feed reader.
 - Disqus is configured to handle comments.

Before you publish your site, **make sure you are using the correct
configuration file** in the `-s` switch to the pelican command. For example:

    :::bash
    pelican content/ -o html -s publishconf.py --debug

#### Set Up S3 Buckets

Here are the steps I took to set up S3 hosting (using the
[S3 console][s3-console] website):

 1. Create S3 bucket names corresponding to my site's domain names:
    `jamesmurty.com` and `www.jamesmurty.com`
 2. Upload the generated site files in the `html/` directory to the bucket
    `jamesmurty.com`. I used my [Synchronize][] application, but any
    S3-compatible file copying program will do.
 3. Visit the bucket's exact *Endpoint* URL as shown in the *Static Website
    Hosting* properties area to make sure everything looks and works properly.

To configure the `www.jamesmurty.com` root domain bucket to redirect requests
to the authoritative `jamesmurty.com` bucket:

 - Edit the bucket Properties and open the *Static Website Hosting* section.
 - Select *Redirect all requests to another host name*
 - Enter the root domain: `jamesmurty.com`

Because my original blog used `/feed/` as the RSS feed endpoint, I also needed
to make this URL path point to the new RSS feed location `/feeds/rss.xml`. This
was easy enough to do with a custom routing rule specified with the following
XML snippet in the *Edit Redirection Rules* section of the *Enable Web Hosting*
properties:

    :::xml
    <RoutingRules>
        <RoutingRule>
            <Condition>
                <KeyPrefixEquals>feed/</KeyPrefixEquals>
            </Condition>
            <Redirect>
                <ReplaceKeyWith>feeds/rss.xml</ReplaceKeyWith>
            </Redirect>
        </RoutingRule>
    </RoutingRules>

#### Set Up DNS using Amazon Route 53

To serve websites from S3 using a root domain, such as a domain without
a leading subdomain prefix like `www` or `blog`, you must use
[Amazon Route 53][route-53] as a DNS server for the site. Unfortunately this
adds to the complexity and cost of S3-hosted websites, but I decided it is
worth the hassle.

The necessary steps are covered in detail in Amazon's
[website hosting][s3-website] instructions, but in brief here's what I did to
set up the domain-to-bucket mappings:

 1. Create a hosted zone for your domain in Route 53
 2. Note the nameservers assigned to that hosted zone (called *Delegation Set*
    in Amazon's console)
 3. Create a record set for the hosted zone
 4. Add an A record alias (*Type: A*, *Alias: Yes*) to the record set to map my
    root domain `jamesmurty.com` to the **Amazon** URL for the authoritative
    S3 bucket, in my case `jamesmurty.com.s3-website-us-east-1.amazonaws.com`.  
    The target bucket should be selectable in the *Alias Target* drop down
    list.
 5. Add a CNAME record to the record set to map the `www.jamesmurty.com`
    subdomain to the root domain `jamesmurty.com`.

Because I was migrating existing domains, at this point I also copied
some additional DNS settings from my original DNS provided over to Route 53,
such as MX mail records.

Once you are happy that the Route 53 settings are correct, set up (or switch
over) the nameservers at your domain name registrar to point to the *Delegation
Set* endpoints you noted above.

Before long, your domain names should resolve to the appropriate S3 buckets and
your static site should be available.


  [blog]: http://jamesmurty.com/
  [blog-subdomain]: http://www.jamesmurty.com/
  [s3]: http://aws.amazon.com/s3/
  [s3-website]: http://docs.aws.amazon.com/AmazonS3/latest/dev/website-hosting-custom-domain-walkthrough.html
  [linode]: http://www.linode.com/
  [static site generator]: http://www.mickgardner.com/2012/12/an-introduction-to-static-site.html
  [pelican]: http://docs.getpelican.com/
  [pelican-pages-import]: https://github.com/getpelican/pelican/pull/858
  [wordpress]: http://www.wordpress.com/
  [virtualenv]: http://www.virtualenv.org/
  [pelican-import-dependencies]: http://docs.getpelican.com/en/3.2/importer.html
  [pandoc]: http://johnmacfarlane.net/pandoc
  [wordpress-export]: http://en.support.wordpress.com/export/
  [cool-uris]: http://www.w3.org/Provider/Style/URI.html
  [pelican-themes]: https://github.com/getpelican/pelican-themes
  [solarized]: http://ethanschoonover.com/solarized
  [s3-console]: https://console.aws.amazon.com/s3/
  [Synchronize]: http://jets3t.org/applications/synchronize.html
  [route-53]: http://aws.amazon.com/route53/
  [disqus]: http://disqus.com/
  [pelican-plugins]: https://github.com/getpelican/pelican-plugins
  [localhost-8000]: http://localhost:8000/
