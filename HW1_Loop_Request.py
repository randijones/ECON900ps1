import requests
from bs4 import BeautifulSoup
import glob
import pandas as pd
import numpy as np
import os
import re
import time
import datetime
from datetime import datetime
import urllib.request
import re


if not os.path.exists("HW1_files"):
	os.mkdir("HW1_files")

if not os.path.exists("HW1_files/historical_data"):
	os.mkdir("HW1_files/historical_data")


f=open('HW1_files/coinmarketcap20190414072535.html' , 'r')
soup=BeautifulSoup(f.read(), features='lxml')

link=[]
coin_name=[]

table = soup.find("table", {"id": "currencies-all"})
tbody = table.find("tbody")
rows = tbody.find_all("tr")
for r in rows:
	name=r.find("td", {"class": "currency-name"}).find("a").text
	currency_name = r.find("td", {"class": "currency-name"}).find("a")
	href=currency_name.get("href")
	#print(href)
	link.append(href)
	coin_name.append(name)
	# print(name)


# for i in range(10):
# 	print(i)

for i in range(500):
	#print(link[i])
	#print(coin_name[i])
	#print('HW1_files/historical_data/' + coin_name[i] + '.html')
	f=open('HW1_files/historical_data/' + coin_name[i] + '.html', 'wb')
	url="https://coinmarketcap.com" + link[i] + "historical-data/" + "?start=20180422&end=20190422"
	#print(url)
	response=urllib.request.urlopen(url)
	html=response.read()
	f.write(html)
	f.close()
	time.sleep(20)





	




