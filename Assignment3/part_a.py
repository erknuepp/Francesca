from html.parser import HTMLParser
from time import sleep

import urllib.request as request
from bs4 import BeautifulSoup
import os

search_page = "https://www.ebay.com/sch/i.html?_nkw=lg+phone&LH_Auction=1&rt=nc&_pgn=1"
result = request.urlopen(search_page)
soup = BeautifulSoup(result, features="lxml")
#sleep(10) #Comment this for testing
with open('ebay_lg_phone_01.htm', 'wb+') as f:
    f.write(soup.prettify("utf-8"))
