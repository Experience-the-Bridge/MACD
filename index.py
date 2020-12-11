"""
Sean O'Brien
-Description: Simple moving averages with the lengths of 9-days, 12-days,
and 26-days. The 9 and 12 day values serve as the dual moving average while
the 26 day is the difference between the 26 and 12 day values. The 26-day
value will be visualized seperately about the y = 0 line for positive and
negative values.
-Using yfinance library. $ pip install yfinance. Using the Public API
(without authentication), you are limited to 2,000 requests per hour per
IP (or up to a total of 48,000 requests a day). Please use time.sleep(1)
to avoid your IP getting blocked.

-Using virtual enviornment with python@3.7 as interpreter
-Column names: Date,Open,High,Low,Close,Volume,Dividends,Stock Splits

-There are more params you can set for history() method:
Arguments           Scenarios                                                                           Example Value
period              date period to download                                                             1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max
interval            data interval. If it’s intraday data, the interval needs to be set within 60 days   1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo
start               If period is not set- Download start date string (YYYY-MM-DD) or 'datetime'         2020-03-18
end                 If period is not set - Download end date string (YYYY-MM-DD) or ''datetime'         2020-03-18
prepost             Boolean value to include Pre and Post market data                                   Default is False
auto_adjust         Boolean value to adjust all OHLC                                                    Default is True
actions             Boolean value download stock dividends and stock splits events                      Default is True

"""

# Import Libraries, assign to reference variables
import yfinance as yf
import html5lib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn
import os
from os import path
import time

# Explicit type cast of variables
uInput1: str
uInput2: str
uInput3: str
tmp1: str
tmp2: str
tmp3: str
beginDate: str
endDate: str

shortTerm: int = 0
mediumTerm: int = 0
longTerm: int = 0

# User inputs
uInput1 = (input("Enter the ticker symbol: "))
tmp1 = uInput1.upper()

uInput2 = (input("Enter the begining date, format YYYY-MM-DD: "))
tmp2 = uInput2

uInput3 = (input("Enter the ending date, format YYYY-MM-DD: "))
tmp3 = uInput3

shortTerm = eval(input("Enter your short-term moving average value: "))
mediumTerm = eval(input("Enter your mid-term moving average value: "))
longTerm = eval(input("Enter your long-term moving average value: "))

filename = (tmp1 + '.csv')

# Download stock data then export as CSV
data_df = yf.download(tmp1, start=tmp2, end=tmp3)
data_df.to_csv(filename)

# Wait until file download completes
pwd  = os.getcwd()
path = (pwd + "/" + filename)
while not os.path.exists(path):
    time.sleep(1)
    print("%s not ready" % path)
else:
    print("%s complete" % path)

# Read in data
underlying = pd.read_csv(filename)

# Visualize the data
plt.figure(figsize=(13, 7))
plt.plot(underlying['Close'], label = tmp1)
plt.title(tmp1 + ' Closing Price History')
plt.xlabel(tmp2 + ' through ' + tmp3)
plt.ylabel('Closing Price USD ($)')
plt.legend(loc = 'upper left')
#plt.show()

# Create the simple short-term moving average

SMAshort = pd.DataFrame()
SMAshort['Close'] = underlying['Close'].rolling(window = shortTerm).mean()

# Create the simple mid-term moving average
SMAmid = pd.DataFrame()
SMAmid['Close'] = underlying['Close'].rolling(window = mediumTerm).mean()

# Create the simple long-term moving average (for the MACD)
SMAlong = pd.DataFrame()
SMAlong['Close'] = underlying['Close'].rolling(window=longTerm).mean()

# Visualize the data
plt.figure(figsize=(13, 7))
plt.plot(underlying['Close'], label = tmp1)
plt.plot(SMAshort['Close'], label = 'Short-term SMA')
plt.plot(SMAmid['Close'], label = 'Medium-term SMA')
plt.plot(SMAlong['Close'], label = 'Long-term SMA')
plt.title(tmp1 + ' Closing Price History')
plt.xlabel(tmp2 + ' through ' + tmp3)
plt.ylabel('Closing Price USD ($)')
plt.legend(loc = 'upper left')
#plt.show()

# Create a new dataframe to combine everything
data = pd.DataFrame()
data['underlying'] = underlying['Close']
data['SMAshort'] = SMAshort['Close']
data['SMAmid'] = SMAmid['Close']
data['SMAlong'] = SMAlong['Close']
# The MACD is the difference between the mid and long SMA values
data['MACD'] = (SMAmid['Close'] - SMAlong['Close'])

# Create a function to give 'arrows' when to buy or sell
def buy_sell(data):
    sigPriceSell=[]
    sigPriceBuy=[]
    flag = -1

    for i in range(len(data)):
        # As the shortSMA passes over the midSMA and is above the longSMA
        if data['SMAshort'][i] > data['SMAmid'][i] and data['SMAshort'][i] > data['SMAlong'][i]:
            if flag != 1:
                sigPriceBuy.append(data['underlying'][i])
                sigPriceSell.append(np.nan) #append nothing
                flag = 1 #I was here
            else:
                sigPriceBuy.append(np.nan)
                sigPriceSell.append(np.nan)
                # As the shortSMA passes over the midSMA and is below the longSMA
        elif data['SMAshort'][i] < data['SMAmid'][i] and data['SMAshort'][i] < data['SMAlong'][i]:
            if flag != 0:
                sigPriceBuy.append(np.nan)
                sigPriceSell.append(data['underlying'][i])
                flag = 0
            else:
                sigPriceBuy.append(np.nan)
                sigPriceSell.append(np.nan)
        else:
            sigPriceBuy.append(np.nan)
            sigPriceSell.append(np.nan)
    return(sigPriceBuy, sigPriceSell)

# Store the buy and sell data into a variable
buy_sell = buy_sell(data)
data['Buy_Signal_Price'] = buy_sell[0]
data['Sell_Signal_Price'] = buy_sell[1]

# Visualize the data and the strategy to buy or sell based on your SMA value inputs
plt.figure(figsize=(14, 8))
plt.title(str(shortTerm) + ", " + str(mediumTerm) + ", " + str(longTerm) + " SMA MACD for Ticker: " + tmp1 )
plt.plot(data['underlying'], label = tmp1, alpha = 0.5)
plt.plot(data['SMAshort'], label = str(shortTerm) + " SMA", alpha = 0.5)
plt.plot(data['SMAmid'], label = str(mediumTerm) + " SMA", alpha = 0.5)
plt.plot(data['SMAlong'], label = str(longTerm) + " SMA", alpha = 0.5)
plt.plot(data['MACD'], label = "MACD")
plt.scatter(data.index, data['Buy_Signal_Price'], label = 'Buy', marker = '^', color = 'green')
plt.scatter(data.index, data['Sell_Signal_Price'], label = 'Sell', marker = 'v', color = 'red')
plt.xlabel('Total Days from ' + tmp2 + ' through ' + tmp3)
plt.ylabel('Closing Price USD ($)')
plt.legend(loc = 'upper left')
plt.hlines(y = 0, xmin = 0, xmax = len(data), colors = 'blue', linestyles='solid', label='MACD', data = None, alpha = 0.6)
plt.show()
