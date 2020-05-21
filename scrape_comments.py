# scrape_comments.py start

# importing the functions for each store page
from get_googleplay_comments import get_googleplay_comments
from get_applestore_comments import get_applestore_comments

import pandas as pd


def scrape_comments(data):
    # how data should be sorted
    appname = data[0]
    # the urls should be given without the 'show reviews' tag
    url_applestore = data[1]
    url_googleplay = data[2]
    timeout = data[3]
    scroll = data[4]

    # appending the 'show comments tag'
    url_applestore_com = url_applestore + '#see-all/reviews'
    url_googleplay_com = url_googleplay + '&showAllReviews=true'

    df_google = get_googleplay_comments(url_googleplay_com, scroll, timeout)
    df_apple = get_applestore_comments(url_applestore_com, scroll, timeout)

    # reading downloads needs to be added here

    df_google.to_excel(appname + '-google.xlsx')
    df_apple.to_excel(appname + '-apple.xlsx')

# scrape_comments.py end
