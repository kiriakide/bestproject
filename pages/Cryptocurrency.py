import streamlit as st
import pandas as pd

#Headings
st.set_page_config(page_title="Crypto", page_icon="🪙", layout="wide" )
st.sidebar.success("select a page above")


st.title ("Cryptocurrency Prices 🪙")
st.caption("This is an interactive widget")
st.markdown("Retrieve the market price of cryptocurrency exchange directly from **Binance Website**")

#API
df = pd.read_json('https://api.binance.com/api/v3/ticker/24hr')

#MarketTable
st.subheader('**Market Acetivity Table**')
st.dataframe(df)

#WidgetForCrryptoSelection
st.header("Select an Exchange Crypto Price to Trade")

col1, col2 = st.columns(2)
with col1:
    st.checkbox("Disable selection of coin", key="disabled")

with col2:
    Select_a_coin = st.selectbox('Select a coin', df.symbol, list(df.symbol).index('ETHBTC'),
                                 disabled=st.session_state.disabled,)

coin_selected = df[df.symbol == Select_a_coin]

#Roundthenumbers
def round_value(input_value):
    if input_value.values > 1:
        a = float(round(input_value, 2))
    else:
        a = float(round(input_value, 8))
    return a

#Showtheselection

coin_price = round_value(coin_selected.weightedAvgPrice)

coin_percent = f'{float(coin_selected.priceChangePercent)}%'

col1.metric(Select_a_coin, coin_price, coin_percent)