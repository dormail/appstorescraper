# a script for testing the apple store comment scrapper
from get_applestore_comments import get_applestore_comments
import pandas as pd

# bvb seite
url = 'https://apps.apple.com/de/app/borussia-dortmund/id454971210#see-all/reviews'

# tu dortmund app seite
url = 'https://apps.apple.com/de/app/internet-browser-firefox/id989804926#see-all/reviews'

#url = '/home/matthiasmaile/Documents/sk/appstoescrapper/apple_testcomments.html'

appname = 'whatsapp'

url = input("Type in the URL: ")
appname = input("Type in the app name: ")

get_applestore_comments(url).to_excel(appname + '.xlsx')
