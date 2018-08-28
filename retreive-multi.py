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
		stock_data = nse.get_quote(stock_code)
	except Exception as e:
		pass
	else:
		today_date = datetime.today().strftime('%Y-%m-%d')
		data_for_today = {}
		data_for_today = {
			"open": stock_data["open"],
			"high": stock_data["dayHigh"],
			"low" : stock_data["dayLow"],
			"close": stock_data["closePrice"]
			}
		min_stock_data[stock_code][today_date] = data_for_today
		with open("files/stock_data_min.json", "w") as jsonFile:
		    json.dump(min_stock_data, jsonFile)
		print("Fetched data for: {0:<20s} |  Competed: {1:3.3f}%".format(stock_code, round(i/len(all_stock_codes)*100,3)))
		i = i+1

if __name__ == '__main__':
	p = Pool(multiprocessing.cpu_count())
	# print("start", datetime.now())
	# p.map(f, list(nse.get_stock_codes().keys()))
	p.map(f, ['3IINFOTECH'])
	# print("end", datetime.now())

	# print("start", datetime.now())
	# for x in nse.get_stock_codes().keys():
	# 	try:
	# 		stock_data = nse.get_quote(x)
	# 	except Exception as e:
	# 		pass

	# 	today_date = datetime.today().strftime('%Y-%m-%d')
	# 	data_for_today = {}
	# 	data_for_today[today_date] = {
	# 		"open": stock_data["open"],
	# 		"high": stock_data["dayHigh"],
	# 		"low" : stock_data["dayLow"],
	# 		"close": stock_data["closePrice"]
	# 		}
	# 	min_stock_data[stock_code] = data_for_today
	# 	with open("files/stock_data_min.json", "w") as jsonFile:
 #    			json.dump(min_stock_data, jsonFile)
	# print("end", datetime.now())
