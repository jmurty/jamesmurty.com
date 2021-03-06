#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u'James'
SITENAME = u'post past :: james murty'
SITESUBTITLE = u'Contemplating the brave new present'
SITEURL = 'http://james.murty.co'

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
STATIC_URL = 'static/{path}'
STATIC_SAVE_AS = 'static/{path}'

FEED_DOMAIN = SITEURL
FEED_RSS = 'feeds/rss.xml'
FEED_ALL_RSS = None
CATEGORY_FEED_RSS = None
TAG_FEED_RSS = 'feeds/tag/%s.rss.xml'
FEED_ATOM = 'feeds/atom.xml'
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TAG_FEED_ATOM = 'feeds/tag/%s.atom.xml'

MENUITEMS = []

# Blogroll
LINKS = None

# Social widget
SOCIAL = []

DEFAULT_PAGINATION = 5
SUMMARY_MAX_LENGTH = None  # Don't summarise

# Static file directories inside content/
STATIC_PATHS = (
    'images',
    'files',
    'robots.txt',
    'images/favicon.ico',
)

# Shift location of static files (instead of easier-to-use but deprecated
# FILES_TO_COPY setting).
EXTRA_PATH_METADATA = {
    # Shift some static files to site root
    'robots.txt': {'path': '../robots.txt'},
    'images/favicon.ico': {'path': '../favicon.ico'},
}

THEME = 'themes/blog'

PLUGIN_PATH = 'pelican-plugins'
PLUGINS = ['sitemap', 'neighbors']

SITEMAP = {
    'format': 'xml',
    'changefreqs': {
        'pages': 'daily',
    }
}

RELATED_POSTS_MAX = 5
