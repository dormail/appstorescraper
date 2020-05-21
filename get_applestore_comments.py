# a script which reads sthe comment page from an ap in the apple app 
# store

# selenium for opening websites
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
# for the timouts
import time
# for analysing the html code
from bs4 import BeautifulSoup
# saving data in pandas.DataFrame
import pandas as pd

# url is the apple store page (note: it has to be the "read more section"
# from the app, not the app page itself). 
# scrolling is the amount of times it should scroll down. Doubling it 
# results in double the amount of commments scraped, but als doubles the 
# runtime.
# timeout sets the time in seconds between each scroll. It scales n:n for
# the runtime, but should be set according to internet speed and compute
# perfomance.
# The function returns a pd.DataFrame with all the comments.
def get_applestore_comments(url, scrolling, timeout):
    browser = webdriver.Firefox()
    page = browser.get(url)

    time.sleep(7)

    for i in range(scrolling):
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(timeout)

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
        dates_list.append(dates_tags[i].contents[0])

    # extracting comment titles
    title_tags = soup.find_all("h3", class_="we-truncate we-truncate--single-line ember-view we-customer-review__title")
    title_list = []
    for i in range(len(title_tags)):
        title_list.append(title_tags[i].contents[0])
    
    # extracting the content from the comment
    # contents can have different classes so I made an array for the class
    # searching by class
    content_tags = soup.find_all("blockquote", class_=["we-truncate we-truncate--multi-line we-truncate--interactive we-truncate--truncated ember-view we-customer-review__body", "we-truncate we-truncate--multi-line we-truncate--interactive ember-view we-customer-review__body", "we-clamp ember-view"])
    # searching by id
    #content_tags = soup.find_all("blockquote", attrs = {"id": "ember554"})
    content_list = []
    for i in range(len(content_tags)):
        content_list.append(content_tags[i].find_all('p')[0].string)

    #testdata = {'content': content_list}
    #test_df = pd.DataFrame(testdata)
    #test_df.to_excel('test.xlsx')
    #print(test_df)

    # extracting the stars given
    # stars a saved inside the tag, so first extracting the tags
    stars_tags = soup.find_all("span", class_=["we-star-rating-stars we-star-rating-stars-1", "we-star-rating-stars we-star-rating-stars-2", "we-star-rating-stars we-star-rating-stars-3", "we-star-rating-stars we-star-rating-stars-4", "we-star-rating-stars we-star-rating-stars-5"])
    stars_list = []
    for i in range(len(stars_tags)):
        stars_list.append(stars_tags[i].attrs['class'][1][-1])

    # from debuggin
    #print(len(title_list))
    #print(len(dates_list))
    #print(len(content_list))
    #print(len(stars_list))

    if len(title_list) != len(dates_list):
        print("len(title_list) != len(dates_list)")
    if len(dates_list) != len(content_list):
        print("len(dates_list) != len(content_list)")

    # creating the data frame for the result
    result = {'date': dates_list, 'title': title_list, 'content': content_list, 'stars': stars_list}
    result = pd.DataFrame(result)

    return result
