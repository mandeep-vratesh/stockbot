from multiprocessing import Pool, TimeoutError
import multiprocessing
import time
import os
from nsetools import Nse
from datetime import datetime
import json

#initializations
nse = Nse()

def f(x):
	try:
		stock_data = nse.get_quote(x)
	except Exception as e:
		pass
	today_date = datetime.today().strftime('%Y-%m-%d')
	data_for_today = {}
	data_for_today[today_date] = {
		"open": stock_data["open"],
		"high": stock_data["dayHigh"],
		"low" : stock_data["dayLow"],
		"close": stock_data["closePrice"]
		}
	min_stock_data[stock_code] = data_for_today
	with open("files/stock_data_min.json", "w") as jsonFile:
	    	json.dump(min_stock_data, jsonFile)


if __name__ == '__main__':
	p = Pool(multiprocessing.cpu_count())
	print("start", datetime.now())
	p.map(f, list(nse.get_stock_codes().keys()))

	print("end", datetime.now())

	print("start", datetime.now())
	for x in nse.get_stock_codes().keys():
		try:
			stock_data = nse.get_quote(x)
		except Exception as e:
			pass

		today_date = datetime.today().strftime('%Y-%m-%d')
		data_for_today = {}
		data_for_today[today_date] = {
			"open": stock_data["open"],
			"high": stock_data["dayHigh"],
			"low" : stock_data["dayLow"],
			"close": stock_data["closePrice"]
			}
		min_stock_data[stock_code] = data_for_today
		with open("files/stock_data_min.json", "w") as jsonFile:
    			json.dump(min_stock_data, jsonFile)
	print("end", datetime.now())
