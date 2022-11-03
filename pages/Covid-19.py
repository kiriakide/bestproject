import streamlit as st
import requests



base_url = "https://api.apify.com/v2/key-value-stores/SmuuI0oebnTWjRTUh/records/LATEST?disableRedirect=true."
weather_data = requests.get(base_url).json()
st.write(weather_data)