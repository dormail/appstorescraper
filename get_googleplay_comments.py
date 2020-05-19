# a script which scrapes the data about comments on the google play store
import requests
from bs4 import BeautifulSoup
import pandas as pd

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

import time

def get_googleplay_comments(url):
    # loading the page with selenium
    browser = webdriver.Firefox()
    browser.get(url)

    time.sleep(7)
    
    # scrolling to bottom to load more comments 30 times
    for i in range(30):
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)

    html = browser.page_source
    browser.quit()

    # loading the html source code into soup and closing selenium
    soup = BeautifulSoup(html, 'html.parser')

    # analysing the soup
    # scraping the dates
    dates_tags = soup.find_all("span", class_="p2TkOb")
    dates_list = []
    for i in range(len(dates_tags)):
        dates_list.append(dates_tags[i].contents[0])

    # scraping the stars given
    stars_tags = soup.find_all("div", attrs = {'aria-label': ["Rated 1 stars out of five stars", "Rated 2 stars out of five stars", "Rated 3 stars out of five stars", "Rated 4 stars out of five stars", "Rated 5 stars out of five stars"]})
    stars_list = []
    for i in range(len(stars_tags)):
        stars_list.append(stars_tags[i].get('aria-label')[6])

    # scraping 'number of times this review was rated helpful'
    helpful_tags = soup.find_all("div", attrs={'aria-label': "Number of times this review was rated helpful"})
    helpful_list = []
    for i in range(len(helpful_tags)):
        helpful_list.append(helpful_tags[i].contents[0])

    # scraping short comments
    shortcomment_tags = soup.find_all("span", attrs={'jsname': "bN97Pc"})
    shortcomment_list = []
    for i in range(len(shortcomment_tags)):
        shortcomment_list.append(shortcomment_tags[i].contents)

    # scraping long content of the review, if available
    comment_tags = soup.find_all("span", attrs={'jsname': "fbQN7e"})
    comment_list = []
    for i in range(len(comment_tags)):
        comment_list.append(comment_tags[i].contents)

    # merging the comment lists
    comments = []
    for i in range(len(comment_list)):
        if comment_list[i] == []:
            comments.append(shortcomment_list[i][0])
        else:
            comments.append(comment_list[i][0])


    # adding everything together into a pandas data frame
    data = {'date': dates_list, 'stars': stars_list, 'helpful': helpful_list, 'comment': comments}
    result = pd.DataFrame(data)

    print(result)
    return result
