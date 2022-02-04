from bs4 import BeautifulSoup
import requests
import time


def main():
    try:
        URL = 'https://www.planespotters.net/user/login'

        HEADERS = {"referer":"https://www.planespotters.net/",
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
        result = requests.get(URL, headers=HEADERS)

        cookies = result.cookies
        print(cookies)
        # Look at the unmodified source.
        #print(result.content + '\n')

        # # Here we extract the token required to login
        soupy = BeautifulSoup(result.content, 'html.parser')
        csrf = soupy.find(id="csrf")['value']
        
        print(csrf)
        

        # # Always pause between two requests.

        time.sleep(5)  # 5s

        # # An open session carries the cookies and allows you to make post requests
        session_requests = requests.session()

        res = session_requests.post(URL,
                                    data={"referer": "https://www.planespotters.net/",
                                          "username": "edward.knueppel.jr@gmail.com",  # your username here
                                          "password": "Cat4sale__--",  # your password here
                                          "csrf": csrf},
                                    headers=HEADERS,
                                    timeout=15)
        # #
        # # This will get us the Cookies.
        # #
        cookies = session_requests.cookies.get_dict()

        # #
        # # And this is the easiest way to remain in session.
        # #
        page2 = session_requests.get(URL, cookies=cookies, headers=HEADERS)

        doc2 = BeautifulSoup(page2.content, 'html.parser')

        print(doc2)
        print(cookies)
        print(bool(doc2.findAll(text="© Planespotters.net 2022. All rights reserved.")))

    except Exception as ex:
        print('error: ' + str(ex))


if __name__ == '__main__':
    main()
