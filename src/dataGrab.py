from yahoo_fin.stock_info import get_data
import pickle
import json
import os
import pandas

#Load ticker list from obj/tickers.dat
script_dir = os.path.dirname(__file__)
with open (f'{script_dir}\\..\\obj\\tickers.dat', 'rb') as f:
    nifty_50_symbols = pickle.load (f)

data = list ()

#API Call to retrieve historical data
for ticker in nifty_50_symbols:
    data.append(get_data(ticker, start_date='01/01/2024', end_date='10/20/2024', interval='1wk').to_json ())


#Serialize DataFrame (dict) to obj/dataframe.json
with open(f'{script_dir}\\..\\obj\\dataframe.json', 'w') as f:
    print((type(data)))
    json.dump(data, f)

