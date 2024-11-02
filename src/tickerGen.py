nifty_50_symbols = ['RELIANCE', 'HDFCBANK', 'ICICIBANK', 'INFY', 'TCS',
                    'HINDUNILVR', 'ITC', 'LT', 'KOTAKBANK', 'AXISBANK',
                    'SBIN', 'BHARTIARTL', 'BAJFINANCE', 'ASIANPAINT', 'MARUTI',
                    'M&M', 'TITAN', 'NTPC', 'TATAMOTORS', 'ULTRACEMCO',
                    'SUNPHARMA', 'NESTLEIND', 'POWERGRID', 'TATASTEEL', 'ONGC',
                    'ADANIENT', 'JSWSTEEL', 'BAJAJFINSV', 'HCLTECH', 'WIPRO',
                    'ADANIPORTS', 'INDUSINDBK', 'GRASIM', 'BRITANNIA', 'CIPLA',
                    'DRREDDY', 'BPCL', 'TECHM', 'EICHERMOT', 'HINDALCO',
                    'TATACONSUM', 'COALINDIA', 'SBILIFE', 'HDFCLIFE', 'DIVISLAB',
                    'HEROMOTOCO', 'BAJAJ-AUTO', 'APOLLOHOSP', 'SHRIRAMFIN', 'LTIM']

for i in range (len(nifty_50_symbols)):
    nifty_50_symbols[i] += '.NS'

import pickle
with open ('..\\obj\\tickers.dat', 'wb') as f:
    pickle.dump (nifty_50_symbols, f)