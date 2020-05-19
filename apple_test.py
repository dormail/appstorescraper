# a script for testing the apple store comment scrapper
from get_applestore_comments import get_applestore_comments
import pandas as pd

url = 'https://apps.apple.com/de/app/borussia-dortmund/id454971210#see-all/reviews'

#url = '/home/matthiasmaile/Documents/sk/appstoescrapper/apple_testcomments.html'

get_applestore_comments(url).to_excel('bvb.xlsx')
