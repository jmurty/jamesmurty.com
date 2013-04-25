#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u'James'
SITENAME = u'post past :: james murty'
SITESUBTITLE = u'Contemplating the brave new present'
SITEURL = 'http://www.jamesmurty.com'

TIMEZONE = 'Australia/Sydney'
DEFAULT_DATE_FORMAT = '%Y-%m-%d'

DEFAULT_LANG = u'en'

OUTPUT_PATH = 'html/'
DISPLAY_PAGES_ON_MENU = True
DEFAULT_CATEGORY = 'Blog'

RELATIVE_URLS = True

ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'
TAG_URL = 'tag/{slug}/'
TAG_SAVE_AS = 'tag/{slug}/index.html'

FEED_DOMAIN = SITEURL
FEED_RSS = 'feed/rss.xml'
CATEGORY_FEED_RSS = None
TAG_FEED_RSS = 'feed/tag/%s.rss.xml'
FEED_ATOM = 'feed/atom.xml'
CATEGORY_FEED_ATOM = None
TAG_FEED_RSS = 'feed/tag/%s.atom.xml'

MENUITEMS = []

# Blogroll
LINKS = None

# Social widget
SOCIAL = []

DEFAULT_PAGINATION = 5
SUMMARY_MAX_LENGTH = None  # Don't summarise

# Static file directories inside content/
STATIC_PATHS = ('images',)

THEME = 'themes/blog'

PLUGIN_PATH = 'pelican-plugins'
PLUGINS = ['sitemap', 'neighbors', 'related_posts']

SITEMAP = {
    'format': 'xml',
    'changefreqs': {
            'pages': 'daily',
    }
}

RELATED_POSTS_MAX = 5
