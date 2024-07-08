import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
table = pd.read_html(url)
sp500 = table[0]
tickers = sp500['Symbol'].tolist()

start_date = '2023-01-01'
end_date = '2024-01-01'
data = yf.download(tickers, start=start_date, end=end_date)['Adj Close']

data.dropna(axis=1, inplace=True)
one_year_returns = (data.iloc[-1] - data.iloc[0]) / data.iloc[0]
top_50_stocks = one_year_returns.nlargest(50)
