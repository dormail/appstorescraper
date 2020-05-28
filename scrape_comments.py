# scrape_comments.py start

# importing the functions for each store page
from get_googleplay_comments import get_googleplay_comments
from get_applestore_comments import get_applestore_comments

from get_googleplay_appdata import get_googleplay_appdata
from get_applestore_appdata import get_applestore_appdata

import pandas as pd


def scrape_comments(data):
    # how data should be sorted
    appname = data[0]
    # the urls should be given without the 'show reviews' tag
    url_applestore = data[1]
    url_googleplay = data[2]
    timeout = data[3]
    scroll = data[4]

    # reading downloads needs to be added here
    #google_appdata = get_googleplay_appdata(url_googleplay)
    #apple_appdata = get_applestore_appdata(url_applestore)

    # appending the 'show comments tag'
    url_applestore_com = url_applestore + '#see-all/reviews'
    url_googleplay_com = url_googleplay + '&showAllReviews=true'

    #df_apple = get_applestore_comments(url_applestore_com, scroll, timeout)
    if (scroll > 8):
        scroll = 8
    df_google = get_googleplay_comments(url_googleplay_com, scroll, timeout)

    # adding meta data to the google df
    #google_downloads = google_appdata[0].replace(",", "").replace(".", "")
    #google_rating = google_appdata[1]
    #df_google.iat[0,0] = int(google_downloads)
    #df_google.iat[1,0] = float(google_rating)
    # adding meta data to apple store df
    #apple_downloads = apple_appdata[0]
    ##apple_raing = apple_appdata[1]
    #df_apple.iat[0,0] = int(apple_downloads)
    #df_apple.iat[1,0] = float(apple_raing)

    df_google.to_excel(appname + '-google.xlsx')
    #df_apple.to_excel(appname + '-apple.xlsx')

# scrape_comments.py end
