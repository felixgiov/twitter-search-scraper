# -*- coding: utf-8 -*-
"""
Created on Sun Apr 30 13:13:38 2017

@author: felix
"""

import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()

url = u'https://twitter.com/search?l=&q=anies%20OR%20sandiaga%20near%3A%22DKI%20Jakarta%22%20within%3A15mi%20since%3A2017-02-16%20until%3A2017-04-17&src=typd'

browser.get(url)
time.sleep(1)

body = browser.find_element_by_tag_name('body')

for _ in range(400):
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.2)
    
tweets = browser.find_elements_by_class_name('tweet-text')

with open('anies-sandi.csv','w', encoding="utf-8") as file:
    for tweet in tweets:
        file.write(tweet.text.replace('\n', ' ').replace(';', ' ').replace(',',' '))
        file.write('\n')
        