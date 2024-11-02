from yahoo_fin.stock_info import get_data
import pickle
import os

#Load ticker list from obj/tickers.dat
script_dir = os.path.dirname(__file__)
with open (f'{script_dir}\\..\\obj\\tickers.dat', 'rb') as f:
    nifty_50_symbols = pickle.load (f)

data = {}

#API Call to retrieve historical data
for ticker in nifty_50_symbols:
    data[ticker] = get_data(ticker, start_date='01/01/2024', end_date='10/20/2024', interval='1wk')


#Pickle DataFrame (dict) to obj/dataframe.dat
with open(f'{script_dir}\\..\\obj\\dataframe.dat', 'wb') as f:
    pickle.dump(data, f)

