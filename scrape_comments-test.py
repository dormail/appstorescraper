# a test for scrape_comments.py

from scrape_comments import scrape_comments

appname = 'anton'
url_apple = 'https://apps.apple.com/de/app/anton-lern-app-grundschule/id1180554775?l=en'
url_google = 'https://play.google.com/store/apps/details?id=biz.arrowstar.funnyfood2&hl=de&showAllReviews=true'

timeout = 2
scroll = 8

data = [appname, url_apple, url_google, timeout, scroll]

scrape_comments(data)
