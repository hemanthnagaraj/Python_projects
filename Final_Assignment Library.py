#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import yfinance as yf
import pandas as pd
import requests
import json
import matplotlib.pyplot as plt

# #Using the yfinance Library to Extract Stock Data#
# #Using the Ticker module we can create an object that will allow 
# #us to access functions to extract data. To do this we need to 
# #provide the ticker symbol for the stock, here the company is Apple 
# #and the ticker symbol is AAPL.

# apple = yf.Ticker("AAPL")

# # #!wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/data/apple.json
# # #outpath = '/Users/hemanthnagaraj/Desktop/Classess/Data_Analysis/Python/'
# # url01 = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/data/apple.json'
# # #apple.json = wget.download(url01, out = outpath)
# # apple_info = requests.get(url01)
# # open('apple.json', 'wb').write(apple_info.content)

# with open('apple.json') as json_file:
#     apple_info = json.load(json_file)
#     # Print the type of data variable    
#     #print("Type:", type(apple_info))
# #print(apple_info)
# #print(type(apple_info))
# print(apple_info['zip'])

# # Extracting Share Price
# # A share is the single smallest part of a company's stock that you can buy, 
# # the prices of these shares fluctuate over time. Using the history() method 
# # we can get the share price of the stock over a certain period of time. 
# # Using the period parameter we can set how far back from the present to 
# # get data. The options for period are 1 day (1d), 5d, 1 month (1mo) , 3mo, 
# # 6mo, 1 year (1y), 2y, 5y, 10y, ytd, and max.

# apple_share_price_data = apple.history(period="max")
# #print(apple_share_price_data)

# print(apple_share_price_data.head())

# apple_share_price_data.reset_index(inplace=True)

# #apple_share_price_data.plot(x="Date", y="Open")
# #plt.show()

# # Extracting Dividends
# # Dividends are the distribution of a companys profits to shareholders. 
# # In this case they are defined as an amount of money returned per share 
# # an investor owns. Using the variable dividends we can get a dataframe of 
# # the data. The period of the data is given by the period defined in the 
# # 'history` function.

# print(apple.dividends)

# apple.dividends.plot()
# plt.show()

amd = yf.Ticker('AMD')
# url02 = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/data/amd.json'
# amd_info = requests.get(url02)
# open('amd.json', 'wb').write(amd_info.content)

with open('amd.json') as json_file:
    amd_info = json.load(json_file)
print(amd_info['country'])
print(amd_info['sector'])

amd_share_price_data = amd.history(period="max")

# print(amd_share_price_data)
print(amd_share_price_data.head())


