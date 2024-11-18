import csv
import pickle
import os

script_dir = os.path.dirname(__file__)
f = open (f'{script_dir}\\..\\obj\\tickers.dat', 'rb')

symbols = pickle.load (f)

with open ('temp.csv') as f:
    reader = csv.reader (f)
    with open ('fmtemp.csv', 'w', newline = '') as g:
        writer = csv.writer (g)
        writer.writerow(symbols)

        values = dict ()
        for i in reader:
            if i[-1] in values:
                values[i[-1]] += [i[4]]
            else:
                values[i[-1]] = [i[4]]

        for i in range (42):
            arr = []
            for k in symbols:
                arr.append(values[k][i])

            writer.writerow(arr)
