import urllib.request as request
from bs4 import BeautifulSoup

for i in range(1):
    index = (str)(i + 10)
    search_page = "https://www.ebay.com/sch/i.html?_nkw=lg+phone&LH_Auction=1&rt=nc&_pgn="+index
    print(search_page)
    result = request.urlopen(search_page)
    soup = BeautifulSoup(result, 'html.parser')

    with open('ebay_lg_phone_' + index + '.htm', 'wb+') as f:
        f.write(soup.prettify("utf-8"))