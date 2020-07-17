import yfinance as yf
import streamlit as st

st.write(""" 
#Simple Stock Price App
Shown are the stock closing price and volume of Google
Based on Tutorial by Chanin Nantasemat on Towards Data Science https://towardsdatascience.com/how-to-build-a-data-science-web-app-in-python-61d1bed65020
""")

tickerSymbol = 'GOOGL'

tickerData = yf.Ticker(tickerSymbol)
tickerDf = tickerData.history(period = '1d', start = '2010-05-31', end = '2020-05-31')
st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)