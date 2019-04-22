from bs4 import BeautifulSoup
import os
import glob
import pandas as pd

if not os.path.exists("parsed_files"):
	os.mkdir("parsed_files")

# df = pd.DataFrame(columns=['scrapping_time','short_name','name','market_cap','price','volume','supply','24H_change'])
df = pd.DataFrame(columns=['time', 'short_name', 'name', 'cap', 'price', 'volume', 'supply', 'percent_change'])


for one_file_name in glob.glob("HW1_files/*.html"):
	print("parsing " + one_file_name)
	scrapping_time = os.path.splitext(os.path.basename(one_file_name))[0].replace("coinmarketcap","")
	f = open(one_file_name, "r")
	soup = BeautifulSoup(f.read(), 'html.parser')
	f.close()
	table = soup.find("table", {"id": "currencies-all"})
	tbody = currencies_table.find("tbody")
	rows = currencies_tbody.find_all("tr")
	for r in currency_rows:
		currency_short_name = r.find("td", {"class": "currency-name"}).find("span",{"class":"currency-symbol"}).find("a").text
		currency_name = r.find("td", {"class": "currency-name"}).find("a",{"class":"currency-name-container"}).text
		currency_market_cap = r.find("td", {"class": "market-cap"})['data-sort']
		currency_price = r.find("a",{"class": "price"}).text
		currency_volume = r.find("a",{"class": "volume"}).text
		currency_supply = r.find("td", {"class": "circulating-supply"})['data-sort']
		currency_change = r.find("td", {"class": "percent-change"})['data-sort']

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



# print(df)
df.to_csv("parsed_files/coinmarketcap_dataset.csv")