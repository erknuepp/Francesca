from bs4 import BeautifulSoup
import requests
import time


def main():
    try:
        HEADERS = {'User-Agent':  
           'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}  
  
 
        URL = "https://planespotters.com/user/login"
        page1 = requests.get(URL, HEADERS)
        print(page1)
        doc1 = BeautifulSoup(page1.content, 'html.parser')
         
        #Look at the unmodified source.
        #              
        print(doc1)
        
        # Here we extract the token required to login
        input = doc1.find(id="#csrf");
        print(input)
        token = input.get("value")
        print(token)
         
        #Always pause between two requests.
                      
        time.sleep(5) # 5s


        #An open session carries the cookies and allows you to make post requests
        session_requests = requests.session()

        res = session_requests.post(URL, 
                                data = {"referer" : "http://flightaware.com/",
                                      "mode" : "login",
                                      "flightaware_username" : "", # your username here
                                      "flightaware_password" : "", # your password here
                                      "token" : token},
                                headers = dict(referer = "http://flightaware.com/"),
                                timeout = 15)
        #
        # This will get us the Cookies.
        # 
        cookies = session_requests.cookies.get_dict()

        #
        # And this is the easiest way to remain in session.
        #
        page2 = session_requests.get(URL,  
                                      cookies=cookies)
        
        doc2 = BeautifulSoup(page2.content, 'html.parser')
        

        print(doc2);
        print();
        print(cookies)
        print(bool(doc2.findAll(text = ""))) # your username here
        print(bool(doc2.findAll(text = " My FlightAware")))
    
    except Exception as ex:
        print('error: ' + str(ex))

if __name__ == '__main__':
    main()