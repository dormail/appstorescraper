# a script which reads sthe comment page from an ap in the apple app 
# store

import requests
from bs4 import BeautifulSoup
import pandas as pd

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

import time

def get_applestore_comments(url):
    browser = webdriver.Firefox()
    page = browser.get(url)

    time.sleep(7)

    for i in range(30):
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)


    html = browser.page_source

    browser.quit()

    # for loading directly from store page
    #page = requests.get(url)

    #print(html)
    
    # getting soup
    soup = BeautifulSoup(html, 'html.parser')

    # for loading from saved source code
    #soup = BeautifulSoup(open('apple_testcomments.html'), 'html.parser')

    # extracting the dates to a list
    dates_tags = soup.find_all("time", class_="we-customer-review__date")
    dates_list = []
    for i in range(len(dates_tags)):
        dates_list.append(dates_tags[i].contents)

    # extracting comment titles
    title_tags = soup.find_all("h3", class_="we-truncate we-truncate--single-line ember-view we-customer-review__title")
    title_list = []
    for i in range(len(title_tags)):
        title_list.append(title_tags[i].contents)
    
    # extracting the content from the comment
    # contents can have different classes so I made an array for the class
    content_tags = soup.find_all("blockquote", class_=["we-truncate we-truncate--multi-line we-truncate--interactive we-truncate--truncated ember-view we-customer-review__body", "we-truncate we-truncate--multi-line we-truncate--interactive ember-view we-customer-review__body"])
    content_list = []
    for i in range(len(content_tags)):
        content_list.append(content_tags[i].find_all('p')[0].string)

    # extracting the stars given
    # stars a saved inside the tag, so first extracting the tags
    stars_tags = soup.find_all("span", class_=["we-star-rating-stars we-star-rating-stars-1", "we-star-rating-stars we-star-rating-stars-2", "we-star-rating-stars we-star-rating-stars-3", "we-star-rating-stars we-star-rating-stars-4", "we-star-rating-stars we-star-rating-stars-5"])
    stars_list = []
    for i in range(len(stars_tags)):
        stars_list.append(stars_tags[i].attrs['class'][1][-1])



    if len(title_list) != len(dates_list):
        print("Fehler beim auslesen")
        print("Listen nicht gleich lang")

    if len(dates_list) != len(content_list):
        print("Fehler beim auslesen")
        print("Listen nicht gleich lang")

    # creating the data frame for the result
    result = {'date': dates_list, 'title': title_list, 'content': content_list, 'stars': stars_list}
    result = pd.DataFrame(result)

    if len(title_list) != len(dates_list) != len(content_list):
        print("Fehler beim auslesen")
        print("Listen nicht gleich lang")

    return result
