# a test for scrape_comments.py

from scrape_comments import scrape_comments

appname = 'whatsapp'
url_apple = 'https://apps.apple.com/de/app/internet-browser-firefox/id989804926'
url_google = 'https://play.google.com/store/apps/details?id=com.whatsapp'

timeout = 2
scroll = 30

data = [appname, url_apple, url_google, timeout, scroll]

scrape_comments(data)
