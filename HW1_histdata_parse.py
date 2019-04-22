from bs4 import BeautifulSoup
import os
import glob
import pandas as pd 

if not os.path.exists("parsed_files"):
	os.mkdir("parsed_files")

df=pd.DataFrame(columns=['date', 'open_price', 'day_high', 'day_low', 'close_price', 'day_volume', 'day_cap'])

for one_file_name in glob.glob("historical_data/*.html"):
	print("parsing"+ one_file_name)
	f=open(one_file_name, "r")
	soup=BeautifulSoup(f.read(), 'html.parser')
	f.close()
	historical_table=soup.find("table", {"class": "table"})
	#print(historical_table)
	tbody= historical_table.find("tbody")
	rows=tbody.find_all("tr")
	for r in rows:
		td_all=r.find_all("td")
		date=td_all[0].text
		#print(date)
		open_price=td_all[1].text
		day_high= td_all[2].text
		day_low=td_all[3].text
		close_price=td_all[4].text
		volume=td_all[5].text
		market_cap=td_all[6].text
		#print(market_cap)

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


