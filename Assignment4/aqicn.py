from bs4 import BeautifulSoup
import requests
import time
import re

def main():
	try:
		URL = "http://aqicn.org/city/shanghai/"
		user_agent = {'User-agent': 'Mozilla/5.0'} 
		page = requests.get(URL, user_agent)
		doc = BeautifulSoup(page.content, "html.parser")
		#
		# We can either try to select the correct table...
		#
		tables = doc('table', {'class':'api'})
		table = tables[0]
		tableWeAreInterestedIn = table.next_sibling
		trs = tableWeAreInterestedIn.select("tr")
		clean = re.compile('</?[^>]*?>')
		for tr in trs[0]:
			html = BeautifulSoup(tr.text, "html.parser")
			cleaned = re.sub(clean, "", str(html))
			print(cleaned)

		print("===========================")

		for i in range(len(trs)):
			tr = trs[i]
			if tr.get('id') is None or (not (tr.get('id').startswith("tr_"))):
				continue
			tds = tr.select("td")
			for td in tds:
				print(td.text + ",")


		print("===========================")
		# 
		# or intelligently select in doc.
		# 

		trs2 = doc.select("tr[id^=tr_]")
		for tr in trs2:
			html = BeautifulSoup(tr.text, "html.parser")
			cleaned = re.sub(clean, "", str(html))
			print(cleaned)

		# saveString(doc)
		# loadString()


	except Exception as ex:
		print("Error:" + str(ex))

def saveString(html, filename="test.html"):
	try:
		file = open(filename,"w")
		file.write(str(html))
		file.close()
	except Exception as ex:
		print('Error: ' + str(ex))


def loadString(f="test.html"):
	try:
		html = open(f, "r", encoding='utf-8').read()
		return(html)
	except Exception as ex:
		print('Error: ' + str(ex))

if __name__ == '__main__':
	main()