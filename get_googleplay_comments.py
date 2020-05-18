# a script which scrapes the data about comments on the google play store
import requests
from bs4 import BeautifulSoup

def get_googleplay_comments(url):
    print('scrapping googleplay comments from ' + url + ' started')
    page = requests.get(url)

    soup = BeautifulSoup(page.text, 'html.parser')
    
    comment_section = soup.find_all(jsname = 'fk8dgd')
    
    print(comment_section)

