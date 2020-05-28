# a script which scrapes the data about comments on the google play store

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
import numpy as np

# url is the google play page (note: it has to be the "read more section"
# from the app, not the app page itself). 
# scrolling is the amount of times it should scroll down. Doubling it 
# results in double the amount of commments scraped, but als doubles the 
# runtime.
# timeout sets the time in seconds between each scroll. It scales n:n for
# the runtime, but should be set according to internet speed and compute
# perfomance.
# The function returns a pd.DataFrame with all the comments.

def get_googleplay_comments(url, scrolling, timeout):
    if scrolling <= 0:
        print('Scrolling invalid value')
        
    # loading the page with selenium
    #browser = webdriver.Firefox()
    #browser.get(url)

    #time.sleep(7)
    #browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    #if (scrolling > 8):
        #print("A high scrolling number can break the programm")
        #print("Tests above 8 failed")
    #
    # scrolling to bottom to load more comments 30 times
    # for the button selenium searches for the Artists link, moves up to 
    # the button and clicks
    # the html parser can not handle more than 8 times scrolling down!
    #for i in range(scrolling):
        # 'show more' button locating with the developer link in the bottom
        #try:
            #artist_link = browser.find_element_by_link_text('Artists')
        ## for german:
        #except selenium.common.exceptions.NoSuchElementException:
            #artist_link = browser.find_element_by_link_text('Entwickler')
        #ActionChains(browser).move_to_element(artist_link).move_by_offset(0,-867/5).click().perform()
        #time.sleep(timeout)
        #browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    #time.sleep(2)
    # exporting source code
    #try:
        #html = browser.find_element_by_tag_name("body").text
    ## sometimes page was to large
    #except selenium.common.exceptions.InvalidArgumentException:
        #print('HTML Export after ' + str(scrolling) + ' scrolls did not work.')
        #print('Trying with ' + str(scrolling-1) + ' scrolls')
        #browser.quit()
        #return get_googleplay_comments(url, scrolling - 1, timeout)

    # loading the html source code into soup and closing selenium
    soup = BeautifulSoup(open("/home/matthiasmaile/Documents/appstorescraper/kindergarten.html"), 'html.parser')

    # analysing the soup
    # scraping the dates
    dates_tags = soup.find_all("span", class_="p2TkOb")
    dates_list = []
    for i in range(len(dates_tags)):
        dates_list.append(dates_tags[i].contents[0])

    # scraping the stars given
    stars_tags = soup.find_all("div", attrs = {'aria-label': ["Mit 1 von fünf Sternen bewertet", "Mit 2 von fünf Sternen bewertet", "Mit 3 von fünf Sternen bewertet", "Mit 4 von fünf Sternen bewertet", "Mit 5 von fünf Sternen bewertet"]})
    stars_list = []
    for i in range(len(stars_tags)):
        stars_list.append(stars_tags[i].get('aria-label')[4])

    # scraping 'number of times this review was rated helpful'
    helpful_tags = soup.find_all("div", attrs={'aria-label': "Gibt an, wie oft die Rezension als hilfreich bewertet wurde"})
    helpful_list = []
    for i in range(len(helpful_tags)):
        helpful_list.append(helpful_tags[i].contents[0])

    ## scraping short comments
    #shortcomment_tags = soup.find_all("span", attrs={'jsname': "bN97Pc"})
    #shortcomment_list = []
    #for i in range(len(shortcomment_tags)):
        #shortcomment_list.append(shortcomment_tags[i].contents)

    ## scraping long content of the review, if available
    #comment_tags = soup.find_all("span", attrs={'jsname': "bN97Pc"})
    ##comment_list = []
    #for i in range(len(comment_tags)):
        #comment_list.append(comment_tags[i].contents)

    # bessere comment suche
    empty_string = ''

    all_comments = soup.find_all("div", class_="UD7Dzf")
    comment_list = []
    for i in range(len(all_comments)):
        if not (all_comments[i].find("span", attrs={'jsname': "fbQN7e"}).contents):
            data = all_comments[i].find("span", attrs={'jsname': "bN97Pc"}).string
            print(1)
            print(data)
            comment_list.insert(-1, data)
        else:
            comment_list.append(all_comments[i].find("span", attrs={'jsname': "fbQN7e"}).string)
    # bessere datumssuche
    comment_header = soup.find_all("div", class_="xKpxId zc7KVe")
    dates_list = []
    for i in range(len(comment_header)):
        dates_list.append(comment_header[i].find("span", class_="p2TkOb").string)
    

    # merging the comment lists
    #comments = []
    #for i in range(len(comment_list)):
        #if comment_list[i] == []:
            #comments.append(shortcomment_list[i][0])
        #else:
            #comments.append(comment_list[i][0])

    # adding everything together into a pandas data frame
    misc = np.zeros(len(dates_list))
    
    print(dates_list[-5:-1])

    print(len(dates_list))
    print(len(stars_list))
    print(len(helpful_list))
    print(len(comment_list))

    data = {'other': misc, 'date': dates_list, 'stars': stars_list, 'helpful': helpful_list, 'comment': comment_list}
    result = pd.DataFrame(data)

    #print(result)
    return result
