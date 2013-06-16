Title: Point Chrome's RSS Subscription Extension to Feedly
Date: 2013-06-16 16:00
Author: James
Tags: Tips
Slug: google-rss-extension-feedly

With Google Reader about to bite the dust, I have been using [Feedly][] as an
alternative and I'm pretty happy with it -- especially since the [Reeder][]
iOS app will [soon support Feedly as its backend][reeder-and-feedly].

As of today, Feedly seems to have switched from using Google Reader as their
backend to their own [Normandy][] infrastructure.

This means that, from this point on, feeds added to Google Reader will no
longer be reflected in Feedly. So it was time for me to reconfigue the Chrome
browser [RSS Subscription Extension][ext] tool to add new feeds directly to
Feedly instead of Google Reader.

To do this:

1. Open the extension's options, e.g. via Tools > Extensions.
2. Hit the *Add...* button to add a new feed reader.
3. Set the *Description* to "Feedly" or whatever you like, and set the *URL* to
   [http://www.feedly.com/home#subscription/feed/%s][feed]
4. Save the new entry, and make sure it's your default.

Thanks to [Christina Davis][kudos] for documenting this process as a comment in
the Reviews section of the extension's home page. Hopefully putting the
instructions here will make it easier for others to find, since I couldn't find
a way to link directly to the comment.


  [Feedly]: http://www.feedly.com/
  [Reeder]: http://reederapp.com/
  [reeder-and-feedly]: http://blog.feedly.com/2013/06/04/feedly-is-listening-the-roadmap-you-helped-us-shape/
  [Normandy]: http://blog.feedly.com/2013/03/14/google-reader/
  [ext]: https://chrome.google.com/webstore/detail/rss-subscription-extensio/nlbjncdgjeocebhnmkbbbdekmmmcbfjd?hl=en
  [kudos]: https://plus.google.com/112623135884038579189
  [feed]: http://www.feedly.com/home#subscription/feed/%s
