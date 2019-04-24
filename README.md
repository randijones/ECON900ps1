# econ9000
econ 9000-machine learning

# Homework 1- scrape data on all currencies from the main page of coinmarketcap.com, as well as historical data from individual currencies. Parse the data and analyze it using regression tools. 

Use HW1_Request.py to scrape data on all currencies from the main page. The basic currency data from this request is located in the file coinmarketcap_dataset.csv

Use HW1_Loop_Request.py to scrape the historical data from the first 500 currencies. The historical data is located in the file historical_dataset.csv

Use HW1_parse.py to parse the data scraped using the HW1_Request.py file. 

Use HW1_histdata_parse.py to parse the historical data scraped for the first 500 currencies. 

Use HW1_regression.py to evaluate the data in the same way that is presented in the write-up. 

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
  This code is requesting the information from the website www.coinmarketcap.com/all/views/all, and it is labeling the HTML files by their timestamp.
  
 # HW1_Loop_Request.py
 ```
 f=open('HW1_files/coinmarketcap20190414072535.html' , 'r')
soup=BeautifulSoup(f.read(), features='lxml')
```
This is telling the computer to open a specific file (it can be any of the htmls scraped in the original request file). It is then telling the computer to use the BeautifulSoup package to read the file.

```
link=[]
coin_name=[]
```
Define two lists, link and coin_name (or whatever you want to call them).
```
table = soup.find("table", {"id": "currencies-all"})
tbody = table.find("tbody")
rows = tbody.find_all("tr")
for r in rows:
	name=r.find("td", {"class": "currency-name"}).find("a").text
	currency_name = r.find("td", {"class": "currency-name"}).find("a")
	href=currency_name.get("href")
```
Find the location of the historical table on the webpage, then locate the href link. Also find the location of the name of the currency (this will be used to name the individual HTML files for each currency's historical data)

```
	link.append(href)
	coin_name.append(name)
```
Append the link list to add the hrefs for each currency. Append the coin_name list to add the name of each currency. 

```
for i in range(500):
	f=open('HW1_files/historical_data/' + coin_name[i] + '.html', 'wb')
	url="https://coinmarketcap.com" + link[i] + "historical-data/" + "?start=20180422&end=20190422"
	response=urllib.request.urlopen(url)
	html=response.read()
	f.write(html)
	f.close()
	time.sleep(20)
```
This code tells the computer to scrape the historical data for the first 500 currencies. The latter half of the currencies are relatively small cryptocurrencies with very little data, so scraping the historical data for them would be pointless. 
For the first 500 currencies, we are naming the HTML file "HW1_files/historical_data/'coin_name'.html"  The last half of the url link, "?start=20180422&end=20190422", simply alters the link to display the historical data for the last year. Finally, we tell the computer to sleep, in this case for 20 seconds, each loop to prevent an over-request error. 

# HW1_parse.py
This is the parsing file for the basic currency info from the main page of the website, coinmarketcap.com/all/views/all. 

```
df = pd.DataFrame(columns=['time', 'short_name', 'name', 'cap', 'price', 'volume', 'supply', 'percent_change'])
```
This line of code is defining the columns that will be used in the csv file for the parsed data. 

```
for one_file_name in glob.glob("HW1_files/*.html"):
	print("parsing " + one_file_name)
	scrapping_time = os.path.splitext(os.path.basename(one_file_name))[0].replace("coinmarketcap","")
	f = open(one_file_name, "r")
	soup = BeautifulSoup(f.read(), 'html.parser')
	f.close()
```
Useing the glob package, this code is telling the computer that we will be parsing all of the files in the HW1_files folder with an .html tag. Adding the print line is optional; it simply allows the person parsing the data to know how far along the program is when it is running. 

```
table = soup.find("table", {"id": "currencies-all"})
	tbody = table.find("tbody")
	rows = tbody.find_all("tr")
	for r in rows:
		currency_short_name = r.find("td", {"class": "currency-name"}).find("span",{"class":"currency-symbol"}).find("a").text
		currency_name = r.find("td", {"class": "currency-name"}).find("a",{"class":"currency-name-container"}).text
		currency_market_cap = r.find("td", {"class": "market-cap"})['data-sort']
		currency_price = r.find("a",{"class": "price"}).text
		currency_volume = r.find("a",{"class": "volume"}).text
		currency_supply = r.find("td", {"class": "circulating-supply"})['data-sort']
		currency_change = r.find("td", {"class": "percent-change"})['data-sort']
```
This part of the code is finding the location of the variables of interest in the table. 

```
		df = df.append({
			'time': scrapping_time, 
			'short_name': currency_short_name,
			'name': currency_name,
			'cap': currency_market_cap,
			'price': currency_price,
			'volume': currency_volume,
			'supply': currency_supply,
			'percent_change': currency_change
			}, ignore_index=True)
```
After locating the variables of interest, we must append the variable columns that were defined defined using the df function at the beginning of the text file. 

```
df.to_csv("parsed_files/coinmarketcap_dataset.csv")
```
Finally, we use the df function to convert the information that we are parsing to a csv file. 

# HW1_histdata_parse.py
We will use this file to parse the historical data from the first 500 currencies into an easy-to-read csv file. 
```
df=pd.DataFrame(columns=['date', 'open_price', 'day_high', 'day_low', 'close_price', 'day_volume', 'day_cap'])
```
Just as in the last parsing file, we want to define the columns that we will be using in our csv file. 
```
for one_file_name in glob.glob("historical_data/*.html"):
	print("parsing"+ one_file_name)
	f=open(one_file_name, "r")
	soup=BeautifulSoup(f.read(), 'html.parser')
	f.close()
```
Again, just as in the last file, we want to define the location of the files that we want to parse. In this case, it is all html files in the historical_data folder of my desktop. The print function is a little more important in this parse file than in the last because it may take several hours to parse all of the files, so knowing the location of the program at any given time will give the user a better understanding of how much more time remains until the program is finished. 
```
	historical_table=soup.find("table", {"class": "table"})
	tbody= historical_table.find("tbody")
	rows=tbody.find_all("tr")
	for r in rows:
		td_all=r.find_all("td")
		date=td_all[0].text
		open_price=td_all[1].text
		day_high= td_all[2].text
		day_low=td_all[3].text
		close_price=td_all[4].text
		volume=td_all[5].text
		market_cap=td_all[6].text
```
Finding the locations of the variables of interest is a bit simpler for the historical data than the basic data from before because the values are all located within 'td' lines, so we can simply direct the computer to parse the data from each numbered 'td' line. 
```
df=df.append({
			'date': date,
			'open_price': open_price,
			'day_high': day_high,
			'day_low': day_low,
			'close_price': close_price,
			'day_volume': volume,
			'day_cap': market_cap
			}, ignore_index=True)

df.to_csv("parsed_files/historical_dataset.csv")
```
Finally, we append the Data Frame columns with the values found in the last part of the code. We then convert the data frame to a csv file for easier reading and future analysis. 

# HW1_regression.py
``
target = df.iloc[:,2].values
data = df.iloc[:,4:6]

print(data.head())
regression = linear_model.LinearRegression()

regression.fit(data, target)

X = [
    [0,0],
    [10,10],
]

results = regression.predict(X)
print(results)
``
The first regression analysis is a simple linear regression with 2 dependent variables, day_low and close_price, and a response variable, open_price. This code tells the computer to identify the response and independent variables from the dataframe, then predict a linear regression of the variables with the values identified (lines 177-180). 

``
N= 300
open_price=df.iloc[:,2]
day_low=df.iloc[:,4]
plt.scatter(day_low, open_price, color='g')
plt.xlabel('day_low')
plt.ylabel('open_price')
plt.show()
``

Output of this code will be the scatter plot of open_price and day_low.

``
N=300
open_price=df.iloc[:,2]
close_price=df.iloc[:,5]
plt.scatter(close_price, open_price, color='r')
plt.xlabel('close_price')
plt.ylabel('open_price')
plt.show()
``

Output of this code will be the scatter plot of open_price and close_price.

``
df['close']=df.iloc[:,5]
print (df['close'])

data=df['close']
target=df['open']
model=sm.OLS(target,data).fit()
predictions=model.predict(data)
model.summary()
``

This code will provide a summary regression table of close_price and open_price, not including a constant.

``
data=df['close']
target=df['open']
data = sm.add_constant(data)
model=sm.OLS(target, data).fit()
predictions=model.predict(data)
model.summary()
``

This code will provide a summary regression table of close_price and open_price, including a constant. 

``
df['close']= df.iloc[:,5]
df['day_high']=df.iloc[:,3]

data=df['close']
target=df['day_high']
data = sm.add_constant(data)
model=sm.OLS(target, data).fit()
predictions=model.predict(data)
model.summary()
``

This code will provide a summary regression table of close_price and day_high, including a constant. 

``
df['close']= df.iloc[:,5]
df['day_low']=df.iloc[:,4]

data=df['close']
target=df['day_low']
data = sm.add_constant(data)
model=sm.OLS(target, data).fit()
predictions=model.predict(data)
model.summary()
``

This code will provide a summary regression table of close_price and day_low, including a constant. 

# That's All Folks!
