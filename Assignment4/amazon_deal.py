def save_string(f, s, append):
    if append:
        try:
            file = open(f,'a')
        except OSError: 
            print('cannot open',f)    
        file.write(s)
    else:
        try:
            file = open(f,'w')
        except OSError: 
            print('cannot open',f)
        file.write(s)

url = "https://www.amazon.com/dp/B07Q6ZWMLR"  
   
HEADERS = {'User-Agent':  
           'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}  
  
 

get_data = requests.get(url, headers= HEADERS)  
  
soup = BeautifulSoup(get_data.text, 'lxml')

timers = soup.select('span[id^=deal_expiry_timer]')

# save_string(open("B07Q32KX3J.htm"), get_data.html(), False)