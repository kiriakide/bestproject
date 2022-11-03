import streamlit as st
import requests




base_url = "https://api.apify.com/v2/key-value-stores/SmuuI0oebnTWjRTUh/records/LATEST?disableRedirect=true."
covid_data = requests.get(base_url).json()
st.write(covid_data)

st.metric(label="Last Updated:", value= (covid_data["data"]["last_update"]))

col1,col2,col3 = st.columns(3)

with col1:
    st.metric(label="Deaths", value=(covid_data["regionData"][0-100]["totalDeaths"]), delta="7300")
