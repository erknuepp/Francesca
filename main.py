import urllib.request as request
from bs4 import BeautifulSoup


DEFAULT_RESULTS_PER_PAGE = 60
'''
Find the number of pages in results
'''
RESULTS_COUNT_SELECTOR = '//*[@id="mainContent"]/div[1]/div/div[2]/div[1]/div[1]/h1/span[1]'
search_page = "https://www.ebay.com/sch/i.html?_nkw=lg+phone&LH_Auction=1&rt=nc&_pgn=1"
result = request.urlopen(search_page)
soup = BeautifulSoup(result, features="lxml")
search_result_count = int(soup.find("h1", {"class": "srp-controls__count-heading"}).find("span").text)
maxPageIndex = int(search_result_count/60)
print(maxPageIndex)

for i in range(maxPageIndex):
    index = str(i + 1)
    search_page = "https://www.ebay.com/sch/i.html?_nkw=lg+phone&LH_Auction=1&rt=nc&_pgn="+index    
    result = request.urlopen(search_page)
    soup = BeautifulSoup(result, features="lxml")
    
    with open('ebay_lg_phone_' + index + '.htm', 'wb+') as f:
        f.write(soup.prettify("utf-8"))
