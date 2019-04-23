# econ9000
econ 9000-machine learning

# Homework 1- scrape data on all currencies from the main page of coinmarketcap.com, as well as historical data from individual currencies. Parse the data and analyze it using regression tools. 

Use HW1_Request.py to scrape data on all currencies from the main page. The basic currency data from this request is located in the file coinmarketcap_dataset.csv

Use HW1_Loop_Request.py to scrape the historical data from the first 500 currencies. The historical data is located in the file historical_dataset.csv

Use HW1_parse.py to parse the data scraped using the HW1_Request.py file. 

Use HW1_histdata_parse.py to parse the historical data scraped for the first 500 currencies. 

# HW1_Reqest.py
```
for i in range(5):
	time_stamp=datetime.datetime.fromtimestamp(time.time()).strftime('%Y%m%d%H%M%S')
	print(str(i) + ": " + time_stamp)
	f=open("HW1_files/coinmarketcap" + time_stamp+".html","wb")
	url='http://www.coinmarketcap.com/all/views/all'
	response=urllib.request.urlopen(url)
	html=response.read()
	f.write(html)
```  
  This code will give you the 


