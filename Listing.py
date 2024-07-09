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

portfolio_size = float(input("Enter the size of your portfolio in USD: "))
equal_weight = portfolio_size / 50
prices = data.iloc[-1][top_50_stocks.index]
num_shares = (equal_weight // prices).astype(int)

prices = data.iloc[-1][top_50_stocks.index]
num_shares = (equal_weight // prices).astype(int)
portfolio = pd.DataFrame({
    'Stock': top_50_stocks.index,
    '1-Year Return': top_50_stocks.values,
    'Price': prices.values,
    'Shares to Buy': num_shares.values,
    'Investment': num_shares.values * prices.values
})
print(portfolio)

plt.figure(figsize=(14, 7))
top_50_stocks.plot(kind='bar', title='Top 50 Stocks by 1-Year Price Momentum')
plt.xlabel('Stock')
plt.ylabel('1-Year Return')
plt.grid(True)
plt.show()

