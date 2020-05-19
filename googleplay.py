# a script scraping comments from the google play store page

# a script for testing the apple store comment scrapper
from get_googleplay_comments import get_googleplay_comments
import pandas as pd

#url = input("Type in the URL ")
#appname = input("Type in the apps name ")

url = 'https://play.google.com/store/apps/details?id=com.whatsapp&showAllReviews=true'

appname = 'whatsapp'

get_googleplay_comments(url).to_excel(appname + '.xlsx')


