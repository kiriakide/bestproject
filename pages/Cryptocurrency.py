import streamlit as st
import pandas as pd

#Headings
st.set_page_config(page_title="Crypto", page_icon=":coin:", layout="wide" )
st.sidebar.success("select a page above")

with st.container():
    st.title ("Cryptocurrency Prices")
    st.subheader("Retrieve the market price of cryptocurrency directly from Binance Website")

df = pd.read_json('https://api.binance.com/api/v3/ticker/24hr')

st.header('**Cryptocurrencies prices table**')
st.dataframe(df)

# Widget (Cryptocurrency selection box)
col1, col2 = st.columns(2)
with col1:
    st.checkbox("Disable selection of coin", key="disabled")

with col2:
    Select_a_coin = st.selectbox('Select a coin', df.symbol, list(df.symbol).index('BTCBUSD'), disabled=st.session_state.disabled,)
    Select_a_coin2 = st.selectbox('Select a coin', df.symbol, list(df.symbol).index('ETHBUSD'))
