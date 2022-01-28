from html.parser import HTMLParser
from time import sleep

import urllib.request as request
from bs4 import BeautifulSoup
import os

ITEM_WRAPPER_SELECTOR = ".s-item"
ITEM_BID_COUNT_SELECTOR = ".s-item__bidCount"
ITEM_LINK_SELECTOR = ".s-item__link"
DEFAULT_RESULTS_PER_PAGE = 60

#Find the number of pages in results
search_page = "https://www.ebay.com/sch/i.html?_nkw=lg+phone&LH_Auction=1&rt=nc&_pgn=1"
result = request.urlopen(search_page)

soup = BeautifulSoup(result, features="lxml")
search_result_count = int(soup.find("h1", {"class": "srp-controls__count-heading"}).find("span").text)
maxPageIndex = int(search_result_count/DEFAULT_RESULTS_PER_PAGE)

if maxPageIndex > 10:
    maxPageIndex = 10

#Create all page files
for i in range(maxPageIndex):
    index = str(i + 1)
    search_page = "https://www.ebay.com/sch/i.html?_nkw=lg+phone&LH_Auction=1&rt=nc&_pgn="+index    
    result = request.urlopen(search_page)
    soup = BeautifulSoup(result, features="lxml")
    #sleep(10) #Comment this for testing
    with open('ebay_lg_phone_' + index + '.htm', 'wb+') as f:
        f.write(soup.prettify("utf-8"))

#Walk all the files to do part 2.C
for file in os.listdir():
    if file.endswith('.htm'):
        with open(file, encoding="utf-8") as fp:
            soup = BeautifulSoup(fp, features="lxml")
            for i in soup.select(ITEM_WRAPPER_SELECTOR):
                print(i.find("a").get_attribute_list("href")[0])
                if i.select_one(ITEM_BID_COUNT_SELECTOR) is not None:
                    print(i.select_one(ITEM_BID_COUNT_SELECTOR).text)
