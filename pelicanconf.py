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
SOCIAL = (('linkedin', 'https://www.linkedin.com/in/kevinarvai'),
          ('github', 'https://github.com/arvkevi'),
          ('twitter', 'https://twitter.com/arvkevi'),
          )

DEFAULT_PAGINATION = 10

MARKUP = ('md', 'ipynb')
#MARKUP = ['md']

PLUGIN_PATHS = ['./plugins/pelican-plugins', './plugins']
PLUGINS = ['assets', 'summary', 'ipynb.markup']
#PLUGINS = [
#    'assets', 
#    'summary',       # auto-summarizing articles
#    'feed_summary',  # use summaries for RSS, not full articles
#    'ipynb.liquid',
#    'liquid_tags.img', 
#    'liquid_tags.video',
#    'liquid_tags.youtube', 
#    'liquid_tags.vimeo',
#    'liquid_tags.include_code',
#    'liquid_tags.notebook',
#    'liquid_tags.literal'
#]


#NOTEBOOK_DIR = 'downloads/notebooks'

THEME = "./themes/pelican-twitchy"

# IPYNB
#IPYNB_IGNORE_CSS=False
IGNORE_FILES = ['.ipynb_checkpoints']
#IPYNB_USE_META_SUMMARY=True


### TWITCHY


# COLORS
BOOTSTRAP_THEME = "spacelab"
PYGMENTS = "native"
#TYPOGRIFY = True

SHARE = False
HIDE_SITENAME = True


DISQUS_SITENAME="arvkevi.github.io"
DISQUS_LOAD_LATER=False

# GOOGLE
GOOGLE_ANALYTICS = "UA-66112939-4" 
#GOOGLE_ANALYTICS_UNIVERSAL = "UA-66112939-4"
#GOOGLE_ANALYTICS_UNIVERSAL_PROPERTY = 4


### TWITCHY ^^^

#JINJA_EXTENSIONS = ['jinja2.ext.i18n']

SHOW_ARCHIVES = True
SHOW_FEED = False  # Need to address large feeds

ENABLE_MATHJAX = True

STATIC_PATHS = ['images', 'figures', 'videos', 'downloads', 'favicon.ico']

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
