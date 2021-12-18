AUTHOR = 'thomascytosis'
SITENAME = 'Oily Fish'
SITEURL = ''

PATH = 'content'
OUTPUT_PATH = 'docs'
TIMEZONE = 'America/Denver'

DEFAULT_LANG = 'en'
THEME = 'chunk'
DISPLAY_CATEGORIES_ON_MENU = True
USE_FOLDER_AS_CATEGORY = True
LOAD_CONTENT_CACHE = False
# Feed generation is usually not desired when developing
#FEED_ALL_ATOM = None
#CATEGORY_FEED_ATOM = None
#TRANSLATION_FEED_ATOM = None
#AUTHOR_FEED_ATOM = None
#AUTHOR_FEED_RSS = None
#PAGE_PATHS = ['pages']
DISPLAY_PAGES_ON_MENU = True
# Related Links
# LINKS = (('Clupeidae Wikipedia', 'https://en.wikipedia.org/wiki/Clupeidae'),
#          ('Adriaticnature', 'https://adriaticnature.com/archives/6439'),
#          ('Sardine Reviews', 'https://sardine.reviews/'),
# )
MENUITEMS = (('About', '/pages/about.html'),
        ('Contact', '/pages/contact.html'),
        ('Recipes', '/pages/recipes.html'),
        ('Home', '/pages/home-page.html'))

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

PLUGINS = [
    # ...
    'minchin.pelican.plugins.nojekyll',
    # ...
]
DISQUS_SITENAME = 'https-thomascytosis-github-io-fishweb'
