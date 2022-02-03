from bs4 import BeautifulSoup
import requests
import time

def main():
	try:
		headers = {'User-agent': 'Mozilla/5.0'} 

		URL = "https://www.usnews.com/"
		page = requests.get(URL, headers=headers)

		doc = BeautifulSoup(page.content, 'html.parser')
		h2 = doc.find('h2', text = "Top Stories")
		links = h2.find_next_sibling().select('a')

		'''
		the following two lines of code was used to realize that Top Story links to one 
		story come in pairs of 3
		'''
		        
		#for l in links:
		#  print(l.get('href'))

		url2ndTopStory = links[3].get('href')
		print('url2ndTopStory: \n', url2ndTopStory)

		'''
		wait 5 seconds before we access US News' servers again
		'''
		        
		time.sleep(5)

		docTopStory = BeautifulSoup(requests.get(url2ndTopStory, 
		                                        headers = headers).content, 
		                                        'html.parser')

		title = docTopStory.find("h1").get_text()
		sentences = docTopStory.find(id = 'ad-in-text-target').get_text().split('.')
		print('title : \n', title)
		print('First three sentences:')
		print(". ".join([sentences[i].strip() for i in range(3)]))

	except Exception as ex:
		print("Error:" + str(ex))

if __name__ == '__main__':
	main()