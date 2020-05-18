# a script which lets you scrape data from comments in google play store

from get_googleplay_comments import get_googleplay_comments
from gp_comments_parser import gp_comments_parser

# a test url
url = 'https://play.google.com/store/apps/details?id=de.tudortmund.app&hl=en_US'

src = 'tet'

get_googleplay_comments(url)
print(gp_comments_parser(src))
