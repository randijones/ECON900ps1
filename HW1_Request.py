import requests
import urllib.request
import os
import time
import datetime
from bs4 import BeautifulSoup



if not os.path.exists("HW1_files"):
	os.mkdir("HW1_files")


for i in range(5):
	time_stamp=datetime.datetime.fromtimestamp(time.time()).strftime('%Y%m%d%H%M%S')
	print(str(i) + ": " + time_stamp)
	f=open("HW1_files/coinmarketcap" + time_stamp+".html","wb")
	url='http://www.coinmarketcap.com/all/views/all'
	response=urllib.request.urlopen(url)
	html=response.read()
	f.write(html)
	f.close()
	time.sleep(900)

	




















