import pandas
import pickle

with open ('..\\obj\\tickers.dat', 'rb') as f:
    nifty_50_symbols = pickle.load (f)
'''nifty_50_symbols = ['RELIANCE', 'HDFCBANK', 'ICICIBANK', 'INFY', 'TCS',
                    'HINDUNILVR', 'ITC', 'LT', 'KOTAKBANK', 'AXISBANK',
                    'SBIN', 'BHARTIARTL', 'BAJFINANCE', 'ASIANPAINT', 'MARUTI',
                    'M&M', 'TITAN', 'NTPC', 'TATAMOTORS', 'ULTRACEMCO',
                    'SUNPHARMA', 'NESTLEIND', 'POWERGRID', 'TATASTEEL', 'ONGC',
                    'ADANIENT', 'JSWSTEEL', 'BAJAJFINSV', 'HCLTECH', 'WIPRO',
                    'ADANIPORTS', 'INDUSINDBK', 'GRASIM', 'BRITANNIA', 'CIPLA',
                    'DRREDDY', 'BPCL', 'TECHM', 'EICHERMOT', 'HINDALCO',
                    'TATACONSUM', 'COALINDIA', 'SBILIFE', 'HDFCLIFE', 'DIVISLAB',
                    'HEROMOTOCO', 'BAJAJ-AUTO', 'APOLLOHOSP', 'SHRIRAMFIN', 'LTIM']'''


data = list ()

with open ('..\\obj\\dataframe.dat', 'rb') as f:
    deserial_data = pickle.load (f)
    for i in nifty_50_symbols:
        data.append(pandas.DataFrame(data = deserial_data[i]))
        #data = pickle.load (f)

