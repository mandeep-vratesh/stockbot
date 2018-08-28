from multiprocessing import Pool, TimeoutError
import multiprocessing
import time
import os
from nsetools import Nse
from datetime import datetime
import json

#initializations
nse = Nse()
all_stock_codes = nse.get_stock_codes() #1626
i = 0

with open('files/stock_data_min.json') as f :
    min_stock_data = json.load(f)

def f(stock_code):
	global i
	global min_stock_data
	try:
		min_stock_data[stock_code]
	except Exception as e:
		min_stock_data[stock_code] = {}
		
	try:
		stock_data = nse.get_quote(stock_code)
	except Exception as e:
		pass
	else:
		today_date = datetime.today().strftime('%Y-%m-%d')
		data_for_today = {
			"open": stock_data["open"],
			"high": stock_data["dayHigh"],
			"low" : stock_data["dayLow"],
			"close": stock_data["closePrice"]
			}
		min_stock_data[stock_code][today_date] = data_for_today
		# with open("files/stock_data_min.json", "w") as jsonFile:
		#     json.dump(min_stock_data, jsonFile)
		print("Fetched data for: {0:<20s} |  Competed: {3} or {1:3.3f}% | {2}".format(stock_code, round(i/len(all_stock_codes)*100,3), str(multiprocessing.current_process()), i))
		i = i+1

if __name__ == '__main__':
	# analytics = {}
	today_date = datetime.today().strftime('%Y-%m-%d')

	checkpoint1 = datetime.now()
	# p = Pool(multiprocessing.cpu_count())
	p = Pool(64)
	p.map(f, list(nse.get_stock_codes().keys()))
	# p.map(f, ['CENTRALBK'])
	with open("files/stock_data_min2.json", "w") as jsonFile:
		    json.dump(min_stock_data, jsonFile)
	checkpoint2 = datetime.now()

	difference = checkpoint2 - checkpoint1

	with open('files/status.json') as f:
		analytics = json.load(f)

	analytics[today_date+"_64"] = str(difference)

	with open('files/status.json', 'w') as jsonFile:
		json.dump(analytics, jsonFile)
