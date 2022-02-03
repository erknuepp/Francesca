from bs4 import BeautifulSoup
import requests
import time


def main():
    try:
        url = 'https://www.planespotters.net/user/login'


        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
        result = requests.get(url, headers=headers)
        
        cookies = result.cookies
        print(cookies)
        # Look at the unmodified source.
        #print(result.content + '\n')

        # # Here we extract the token required to login
        soupy = BeautifulSoup(result.content, 'html.parser')
        token = soupy.find(id="csrf")['value'];

        #print(token)

        # # Always pause between two requests.

        time.sleep(5) # 5s

        # # An open session carries the cookies and allows you to make post requests
        #session_requests = requests.session()

        # res = session_requests.post(URL,
        #                         data = {"referer" : "https://www.planespotters.net",
        #                               "mode" : "login",
        #                               "flightaware_username" : "", # your username here
        #                               "flightaware_password" : "", # your password here
        #                               "token" : token},
        #                         headers = dict(referer = "http://flightaware.com/"),
        #                         timeout = 15)
        # #
        # # This will get us the Cookies.
        # #
        # cookies = session_requests.cookies.get_dict()

        # #
        # # And this is the easiest way to remain in session.
        # #
        # page2 = session_requests.get(URL,
        #                               cookies=cookies)

        # doc2 = BeautifulSoup(page2.content, 'html.parser')

        # print(doc2);
        # print();
        # print(cookies)
        # print(bool(doc2.findAll(text = ""))) # your username here
        # print(bool(doc2.findAll(text = " My FlightAware")))

    except Exception as ex:
        print('error: ' + str(ex))

if __name__ == '__main__':
    main()
