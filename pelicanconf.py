AUTHOR = 'thomascytosis'
SITENAME = 'Oily Fish'
SITEURL = '.'

PATH = 'content'
OUTPUT_PATH = 'docs'
TIMEZONE = 'America/Denver'

DEFAULT_LANG = 'en'
THEME = 'chunk'

# Feed generation is usually not desired when developing
#FEED_ALL_ATOM = None
#CATEGORY_FEED_ATOM = None
#TRANSLATION_FEED_ATOM = None
#AUTHOR_FEED_ATOM = None
#AUTHOR_FEED_RSS = None

# Related Links
LINKS = (('Clupeidae Wikipedia', 'https://en.wikipedia.org/wiki/Clupeidae'),
         ('Adriaticnature', 'https://adriaticnature.com/archives/6439'),
         ('Sardine Reviews', 'https://sardine.reviews/'),
)

# Social widget
SOCIAL = (('upcoming...', '#'),
)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

PLUGINS = [
    # ...
    'minchin.pelican.plugins.nojekyll',
    # ...
]
DISQUS_SITENAME = 'https-thomascytosis-github-io-fishweb'
