#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Kevin Arvai'
SITENAME = 'Blogging Bioinformatics'
#SITEURL = 'http://arvkevi.github.io'
SITEURL = 'http://localhost:8000'

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

MARKUP = ('md', 'ipynb')

PLUGIN_PATHS = ['./plugins', './plugins/pelican-plugins']
PLUGINS = ['assets', 'sitemap', 'disqus_static', 'share_post', 'ipynb.markup']

THEME = "./themes/pelican-blue"

TWITTER_USERNAME = 'arvkevi'
GITHUB_USERNAME = 'arvkevi'
STACKOVERFLOW_ADDRESS = 'http://stackoverflow.com/users/'
SHOW_ARCHIVES = True
SHOW_FEED = False  # Need to address large feeds

ENABLE_MATHJAX = True

STATIC_PATHS = ['images', 'figures', 'videos', 'downloads', 'favicon.ico']


# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
