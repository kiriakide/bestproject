import streamlit as st
import requests

#Headings
st.set_page_config(page_title="Crypto", page_icon=":coin:", layout="wide" )

with st.container():
    st.title ("Cryptocurrency")
    st.subheader("Find out ")

st.sidebar.success("select a page above")
url = "https://the-cocktail-db.p.rapidapi.com/search.php"

querystring = {"s":"vodka"}

headers = {
	"X-RapidAPI-Key": "042e82a4c2msh38a9f638f7c9e75p141557jsn7c288a2c34e7",
	"X-RapidAPI-Host": "the-cocktail-db.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)
crypto_data = response.json()
st.write(crypto_data)

option = st.selectbox ('Select currency for price', ('USD', 'BTC', 'ETH'))
st.write('You selected',option)