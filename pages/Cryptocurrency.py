import streamlit as st
import pandas as pd

#Headings
st.set_page_config(page_title="Crypto", page_icon="🪙", layout="wide" )
st.sidebar.success("select a page above")

with st.container():
    st.title ("Cryptocurrency Prices 🪙")
    st.subheader("Retrieve the market price of cryptocurrency directly from Binance Website")

df = pd.read_json('https://api.binance.com/api/v3/ticker/24hr')

st.header('**Cryptocurrencies prices table**')
st.dataframe(df)

col1, col2 = st.columns(2)
with col1:
    st.checkbox("Disable selection of coin", key="disabled")

with col2:
    Select_a_coin = st.selectbox('Select a coin', df.symbol, list(df.symbol).index('ETHBTC'),
                                 disabled=st.session_state.disabled,)

col1_df = df[df.symbol == Select_a_coin]


def round_value(input_value):
    if input_value.values > 1:
        a = float(round(input_value, 2))
    else:
        a = float(round(input_value, 8))
    return a


col1_price = round_value(col1_df.weightedAvgPrice)

col1_percent = f'{float(col1_df.priceChangePercent)}%'

col1.metric(Select_a_coin, col1_price, col1_percent)