import imp
import yfinance as yf
import streamlit as st
import pandas as pd


st.write("""
# Stock Price App 

#### $Shown are the stock closing price and volume of ***Apple!***
"""
)

symbl1 = 'AAPL'

symblData1 = yf.Ticker(symbl1)

Dataframe1 = symblData1.history(period='id',start='2010-5-31', end='2020-5-31')
st.write("""
### Closing Price

"""
)
st.line_chart(Dataframe1.Close)
st.write("""
### Closing Price

"""
)
st.line_chart(Dataframe1.Volume)

st.write("""

#### $Shown are the stock closing price and volume of ***Google!***
"""
)

symbl = 'GOOGL'

symblData = yf.Ticker(symbl)

Dataframe = symblData.history(period='id',start='2010-5-31', end='2020-5-31')
st.write("""
### Closing Price

"""
)
st.line_chart(Dataframe.Close)
st.write("""
### Closing Price

"""
)
st.line_chart(Dataframe.Volume)