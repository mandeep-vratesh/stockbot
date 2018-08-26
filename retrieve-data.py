#imports
from nsetools import Nse
from datetime import datetime
import json
from pprint import pprint

#initializations
nse = Nse()
i = 0 

all_stock_codes = nse.get_stock_codes() #1626

with open('files/stock_data_min.json') as f :
    min_stock_data = json.load(f)
    # print(json.dumps(min_stock_data, indent=4, sort_keys=True))

# TODO: make this multithreaded
for stock_code in all_stock_codes : 
    try:
        stock_data = nse.get_quote(stock_code)
    except Exception as e:
        print(str(e), " for ", stock_code)
        continue
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
    print("Fetched data for: {0:<20s} |  Competed: {1:3.3f}%".format(stock_code, round(i/len(all_stock_codes)*100,3)))
    i = i+1
    
"""
{
    "TITAN": {
        "2018-08-26": {
            "open": 100,
            "high": 100,
            "low" : 40,
            "close": 0
        },
        "2018-08-25": {
            "open": 0,
            "high": 100,
            "low" : 40,
            "close": 100
        },
        "2018-08-24": {
            "open": 100,
            "high": 150,
            "low" : 95,
            "close": 130
        }
    }
}
"""