import streamlit as st
import requests
import pandas as pd



base_url = "https://api.apify.com/v2/key-value-stores/SmuuI0oebnTWjRTUh/records/LATEST?disableRedirect=true."
covid_data = requests.get(base_url).json()
st.write(covid_data)

st.metric(label="Last Updated:", value= (covid_data["data"]["last_update"]))

col1,col2,col3 = st.columns(3)

with col1:
    st.metric(label="Deaths", value=(covid_data["regionData"][0-100]["totalDeaths"]), delta="7300")
with col2:
    st.metric(label="Recovered", value=(covid_data["data"]["recovered"]), delta="23539")
with col3:
    st.metric(label="Active", value=(covid_data["data"]["active"]), delta="50156")

