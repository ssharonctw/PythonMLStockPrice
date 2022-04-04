#Webapp built using streamlit and python
#obtaining data dynamically from the yfinance library where it retreive stock data directly from yahoo finance
#we then utilize streamlit to draw the input into line charts of closing price and volume

import yfinance as yf
import streamlit as st

#below is written in markdown language, can find below for syntax
#https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet
st.write("""
# Simple Stock Price App
Shown are the stock **closing price** and **volume** of Google!
""")

# https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75
#define the ticker symbol
tickerSymbol = 'GOOGL'
#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)#retreive historical data on google stock price
#get the historical prices for this ticker with period = 1 date & specific start date end date
tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2020-5-31')
# Open	High	Low	 Close	Volume	Dividends	Stock Splits
st.write("""
## Closing Price
""")
st.line_chart(tickerDf.Close)
st.write("""
## Volume
""")
st.line_chart(tickerDf.Volume)
