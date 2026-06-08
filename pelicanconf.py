import os

AUTHOR = 'Robert Henderson'
SITENAME = 'Robert Henderson'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Phoenix'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ('CV', 'resources/CV/CV_Henderson.pdf'),
)

# Social widget
SOCIAL = ()

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

THEME = 'theme/rhenderson'

ARTICLE_PATHS = ['papers']
PAGE_PATHS = ['pages']

# Ensure resources are copied over
STATIC_PATHS = ['resources', 'css', 'js', 'fonts', 'navbar.css']

# URL settings
ARTICLE_URL = 'papers/{slug}.html'
ARTICLE_SAVE_AS = 'papers/{slug}.html'
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'

# Index (papers list) should be papers.html
INDEX_SAVE_AS = 'papers.html'

# Home page will be handled by a page with slug 'index'
DIRECT_TEMPLATES = ['index']
