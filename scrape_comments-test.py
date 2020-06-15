# a test for scrape_comments.py

from scrape_comments import scrape_comments

appname = 'anton'
url_google = 'https://play.google.com/store/apps/details?id=com.solocode.anton&hl=de'
url_apple = 'https://apps.apple.com/de/app/anton-schule-lernen/id1180554775'

timeout = 2
scroll = 4

data = [appname, url_apple, url_google, timeout, scroll]

scrape_comments(data)
