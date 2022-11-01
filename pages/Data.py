import streamlit as st
import pandas as pd
import requests

# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey=demo'
r = requests.get(url)
data = r.json()
st.write(data)

#st.json(data)
name = data['Meta Data']['2. Symbol']
open = data['Time Series (Daily)']['2022-10-28']['1. open']
st.write("Name:", name)
st.write("Open:", open)
