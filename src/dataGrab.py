from yahoo_fin.stock_info import get_data
import pickle
import os
import csv

#Load ticker list from obj/tickers.dat
script_dir = os.path.dirname(__file__)
with open (f'{script_dir}\\..\\obj\\tickers.dat', 'rb') as f:
    nifty_50_symbols = pickle.load (f)

data = list ()

#API Call to retrieve historical data
for ticker in nifty_50_symbols:
    data.append(get_data(ticker, start_date='01/01/2024', end_date='11/19/2024', interval='1mo'))

#Add all data to a single CSV file
with open (f'{script_dir}\\..\\obj\\dataframe_monthly.csv', 'w', newline = '') as f:
    w = csv.writer (f)
    w.writerow (nifty_50_symbols)
    for i in range (len (data[0])): #WEEKS
        arr = []
        for j in range (len (data)): #SHARES
            arr.append(data[j]["close"][i])
        w.writerow (arr)


