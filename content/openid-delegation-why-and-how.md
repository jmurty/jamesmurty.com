Title: OpenID Delegation: Why and How
Date: 2009-06-16 15:00
Author: James
Tags: OpenID, Tips
Slug: openid-delegation-why-and-how

The great promise of the [OpenID][] specification is that it can
simplify identity management on the 'net. At its best, OpenID provides
three great features:

### Unified Identity

A single account (identity) with which you can log in to many sites,
removing the need to create and remember a separate username/login for
every web site you interact with.

### Openness

A decentralized authentication system with multiple providers. This
means that you can choose a provider (or even a few) from the [many
options available][] to vouch for your identity, and switch providers if
you find a better one. Or you can even be your own provider.

### Delegation

I think Delegation is the most attractive feature of OpenID because it
means your own web site can act as your identity, while delegating the
authentication process to one (or more) OpenID providers.

In short, with delegation you can log in to sites using a URL you own
like *james.murty.co*, while taking advantage of the strong
authentication options offered by providers such as [Verisign's PIP][].
Although my Verisign PIP identity happens to be
*jmurty.pip.verisignlabs.com*, I can use my own web site as an alias for
this provider-specific identity.

By decoupling your identity from your OpenID provider you can take
advantage of the fact there are many providers and easily switch
providers later on without losing your identity, and without having to
update your associated OpenID identity on every web site. After all, if
you had to do that you might as well have created your own
username/password on every site in the first place.

### But...

Unfortunately, the complexity of OpenID and the challenge ordinary
people can have getting it to work properly is preventing widespread
adoption of the system in general, and of the Openness and Delegation
features in particular. Although big players like Google and Yahoo are
supporting (parts of) the specification, they are understandably
encouraging people to adopt their branded OpenID identities rather than
extolling the advantages of controlling your own identity.

After all, every web company would love to take on the "burden" of
managing your unified web identity. It's the ultimate in vendor lock-in.

### Setup OpenID delegation for your web site

If you have your own web site or blog and are able to edit the HTML
pages directly, you can set up delegation by adding special
`link` tags to the `head` section of one of your
site's pages. You will most likely want to do this on the site's home
page so you can use a short URL like *james.murty.co* instead of
*james.murty.co/my-openid-page.html*.

Below are the `link` tags I use on my site to delegate to my
*jmurty* Verisign PIP identity. You will need to use your own
provider-specific identity URL in your links, and the format could vary
quite a lot depending on the OpenID provider you choose so check your
provider's documentation. Also, I'm not sure that all OpenID providers
actually support delegation, so you should research this before you sign
up with a provider.

    :::html
    <link rel="openid.server"
          href="http://pip.verisignlabs.com/server" />
    <link rel="openid.delegate"
          href="http://jmurty.pip.verisignlabs.com/" />
    <link rel="openid2.provider"
          href="http://pip.verisignlabs.com/server" />
    <link rel="openid2.local_id"
          href="http://jmurty.pip.verisignlabs.com/" />

It is important that these `link` tags be included inside a
valid HTML `head` section in your web page, or many web sites
will be unable to find your delegate settings.

### More Complexity, aka Taming Blogger.com

You may have noticed that the OpenID information is provided twice, once
for the original OpenID specification (`openid.*` tags) and
again for version 2 of the spec (`openid2.*` tags).

I don't know why the second lot of settings is necessary, since
presumably the spec is supposed to be backwards-compatible, but I have
found that some sites won't work properly unless the version 2 settings
are provided.

One example of version incompatibility quirks is Google's Blogger.com,
which allows you to comment on blog posts after logging in with an
OpenID. Prior to adding the `openid2.*` tags I found that
although Blogger would allow me to authenticate and post comments, it
would replace my delegating identity *james.murty.co* with the delegated
version *jmurty.pip.verisignlabs.com*. This meant that the delegation
was essentially useless, since anyone clicking on the nickname for my
comment would end up at an empty Verisign PIP landing page instead of my
own site.

I'm not sure if this is Google's fault, or a fault in the OpenID spec.
Either way it was annoying having to track down and fixing this issue.
It just serves as yet another example where OpenID is not quite living
up to the promise of simplifying identity management.

  [OpenID]: http://openid.net/
  [many options available]: http://openid.net/get/
  [Verisign's PIP]: https://pip.verisignlabs.com/
