#imports
from nsetools import Nse
from datetime import datetime
import json
import csv
import pandas
import time
from multiprocessing import Process
from stockstats import StockDataFrame

#initializations
nse = Nse()
sym = 'titan'
required_quote_info = json.load(open(sym+'.json', 'r'))
"""
{
    "last_price": {
        "1" : 1029,
        "2" : 1220
    }
}
{
    "open": {
        
    },
    "high": {
        
    },
    "low": {
        
    },
    "close": {
        
    },
    "volume": {
        
    }
}
"""

for i in range(2):
    #get the full quote
    full_quote = nse.get_quote(sym)

    #strip to the required information
    required_quote_info['open'][str(datetime.now())] = full_quote['open']
    required_quote_info['high'][str(datetime.now())] = full_quote['dayHigh']
    required_quote_info['low'][str(datetime.now())] = full_quote['dayLow']
    required_quote_info['close'][str(datetime.now())] = full_quote['closePrice']
    required_quote_info['volume'][str(datetime.now())] = full_quote['totalTradedVolume']
    
    print(required_quote_info)
    #request after every 10secs
    time.sleep(5)

# def get_data_and_write_to_file():
#     #get the full quote
#     full_quote = nse.get_quote(sym)

#     #strip to the required information
#     required_quote_info['last_price'][str(datetime.now())] = full_quote['lastPrice']
    
#     #request after every 10secs
#     time.sleep(10)

#update the file
with open(sym+'.json', 'a') as f:
    json.dump(required_quote_info, f)


# #Read CSV File
# def read_csv(file, json_file, format):
#     csv_rows = []
#     with open(file) as csvfile:
#         reader = csv.DictReader(csvfile)
#         title = reader.fieldnames
#         for row in reader:
#             csv_rows.extend([{title[i]:row[title[i]] for i in range(len(title))}])
#         write_json(csv_rows, json_file, format)

# #Convert csv data into json and write it
# def write_json(data, json_file, format):
#     with open(json_file, "w") as f:
#         if format == "pretty":
#             f.write(json.dumps(data, sort_keys=False, indent=4, separators=(',', ': '),ensure_ascii=False))
#         else:
#             f.write(json.dumps(data))

# p = pandas.read_json('infy.json')
# p_historical_json = pandas.read_json('converted.json')
# p_historical_csv = pandas.read_csv('historical.csv')
# # print(p_historical)
# read_csv('historical.csv', 'converted.json', 'pretty')
# stock = StockDataFrame.retype(p)
# print(stock['macd'])

# stock_json = StockDataFrame.retype(p_historical_json)
# stock_csv = StockDataFrame.retype(p_historical_csv)
# print(stock_json['macd'])
# print("yolo")
# print(stock_csv['macd'])