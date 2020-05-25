# get_applestore_appdata.py start 

# selenium as a framework for opening websites
import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
# for timeouts between scrolling down
import time
# beatifulSoup for analysing the html code
from bs4 import BeautifulSoup
# return in pandas dataframe
import pandas as pd
# for removing letters
from remove_letters import remove_letters

def get_applestore_appdata(url):
    result = []

    # loading the page with selenium
    browser = webdriver.Firefox()
    browser.get(url)
    # getting html source code, closing selenium
    time.sleep(2)
    html = browser.page_source
    browser.quit()
    # loading the html source code into soup
    soup = BeautifulSoup(html, 'html.parser')
    
    # amount of downloads
    #downloads = soup.find("span", class_="AYi5wd TBRnV")
    #downloads = downloads.find("span", class_="").contents[0]
    #print(downloads)
    downloads = 0
    result.insert(0, downloads)

    # average rating
    rating = soup.find("span", class_="we-customer-ratings__averages__display").contents[0]
    rating = remove_letters(rating).replace(',', '.')
    #print(rating)

    result.insert(1, rating)
    return result

# get_applestore_appdata.py end
