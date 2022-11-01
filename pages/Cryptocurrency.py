import streamlit as st
import requests

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