import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
# Simple Stock Price App
Below shown are the stock **Closing Price** and **Volume Price** of Google!
""")

#define the ticker symbol
tickerSymbol='GOOGL'

#get data on this ticker
tickerData=yf.Ticker(tickerSymbol)

#get historical prices for this ticker
tickerDf=tickerData.history(period="1d", start="2010-5-31", end="2020-5-31")

#Open High Low Close Volume Dividends Stock Splits

st.write("""
## Closing Price
""")
st.line_chart(tickerDf.Close)

st.write("""
## Volume Price
""")
st.line_chart(tickerDf.Volume)
