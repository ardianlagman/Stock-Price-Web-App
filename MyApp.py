# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import yfinance as yf 
import streamlit as st 


# %%
st.write(""" 
# Simple Stock Price App
Shown are the stock closing price and volume of Google
Based on tutorial by Chanin Nantasenamat on Towards Data Science https://towardsdatascience.com/how-to-build-a-data-science-web-app-in-python-61d1bed65020
""")

# %% [markdown]
# # Define the ticker symbol and retrieve he opening and closing price

# %%
tickerSymbol = 'GOOGL'


# %%
tickerData = yf.Ticker(tickerSymbol)
tickerDf = tickerData.history(period = '1d', start = '2010-05-31', end = '2020-05-31')
st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)


# %%



