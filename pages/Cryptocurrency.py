import streamlit as st
import requests
import pandas as pd

#Headings
st.set_page_config(page_title="Crypto", page_icon=":coin:", layout="wide" )

with st.container():
    st.title ("Cryptocurrency")
    st.subheader("Find out ")

st.sidebar.success("select a page above")

url = "https://api.binance.com/api/v3/ticker/24hr"
r = requests.get(url)
data = r.json()
st.write(data)

option = st.selectbox ('Select currency for price', ('USD', 'BTC', 'ETH'))
st.write('You selected',option)


# Custom function for rounding values
def round_value(input_value):
    if input_value.values > 1:
        a = float(round(input_value, 2))
    else:
        a = float(round(input_value, 8))
    return a

col1, col2, col3 = st.columns(3)

# Widget (Cryptocurrency selection box)
col1_selection = st.sidebar.selectbox('Price 1', url.symbol, list(url.symbol).index('BTCBUSD') )
col2_selection = st.sidebar.selectbox('Price 2', url.symbol, list(url.symbol).index('ETHBUSD') )
col3_selection = st.sidebar.selectbox('Price 3', url.symbol, list(url.symbol).index('BNBBUSD') )
col4_selection = st.sidebar.selectbox('Price 4', url.symbol, list(url.symbol).index('XRPBUSD') )
col5_selection = st.sidebar.selectbox('Price 5', url.symbol, list(url.symbol).index('ADABUSD') )
col6_selection = st.sidebar.selectbox('Price 6', url.symbol, list(url.symbol).index('DOGEBUSD') )
col7_selection = st.sidebar.selectbox('Price 7', url.symbol, list(url.symbol).index('SHIBBUSD') )
col8_selection = st.sidebar.selectbox('Price 8', url.symbol, list(url.symbol).index('DOTBUSD') )
col9_selection = st.sidebar.selectbox('Price 9', url.symbol, list(url.symbol).index('MATICBUSD') )

