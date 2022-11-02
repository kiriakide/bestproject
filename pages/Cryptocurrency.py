import streamlit as st
import pandas as pd

#Headings
st.set_page_config(page_title="Crypto", page_icon=":coin:", layout="wide" )

with st.container():
    st.title ("Cryptocurrency")
    st.subheader("Find out ")

st.sidebar.success("select a page above")

df = pd.read_json('https://api.binance.com/api/v3/ticker/24hr')


st.header('**Table**')
st.dataframe(df)

# Widget (Cryptocurrency selection box)
Select_a_coin = st.selectbox('Price 1', df.symbol, list(df.symbol).index('BTCBUSD') )
col2_selection = st.sidebar.selectbox('Price 2', df.symbol, list(df.symbol).index('ETHBUSD') )
col3_selection = st.sidebar.selectbox('Price 3', df.symbol, list(df.symbol).index('BNBBUSD') )

