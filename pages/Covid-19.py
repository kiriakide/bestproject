import streamlit as st
import requests
import pandas as pd



base_url = "https://api.apify.com/v2/key-value-stores/SmuuI0oebnTWjRTUh/records/LATEST?disableRedirect=true."
covid_data = requests.get(base_url).json()
st.write(covid_data)


df = pd.read_json("https://api.apify.com/v2/key-value-stores/SmuuI0oebnTWjRTUh/records/LATEST?disableRedirect=true.")

#MarketTable
st.header('**Market Acetivity Table**')
st.dataframe(df)