import streamlit as st
import requests

#Headings
st.set_page_config(page_title="Crypto", page_icon=":coin:", layout="wide" )

with st.container():
    st.title ("Cryptocurrency")
    st.subheader("Find out ")

st.sidebar.success("select a page above")


url = "https://bravenewcoin.p.rapidapi.com/ohlcv"

querystring = {"size":"10"}

headers = {
	"Authorization": "Bearer <append token here>",
	"X-RapidAPI-Key": "042e82a4c2msh38a9f638f7c9e75p141557jsn7c288a2c34e7",
	"X-RapidAPI-Host": "bravenewcoin.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)
crypto_data = response.json()
st.write(crypto_data)