import streamlit as st
import requests

#Headings
st.set_page_config(page_title="Covid Cases", page_icon=":anger:", layout="wide" )

with st.container():
    st.title ("Covid Cases 🦠")
    st.header("Get the latest data about covid-19")

st.sidebar.success("select a page above")

#Apiimport
base_url = "https://api.apify.com/v2/key-value-stores/SmuuI0oebnTWjRTUh/records/LATEST?disableRedirect=true."
covid_data = requests.get(base_url).json()
st.write(covid_data)

#widget
col1,col2,col3 = st.columns(3)

with col1:
    st.metric(label="Total Cases", value=(covid_data["regionData"][0-100]["totalCases"]), delta=(covid_data["regionData"][0-100]["newCases"]))
with col2:
    st.metric(label="Deaths", value=(covid_data["regionData"][0-100]["totalDeaths"]), delta=(covid_data["regionData"][0-100]["newDeaths"]))
with col3:
    st.metric(label="Recovered", value=(covid_data["regionData"][0 - 100]["totalRecovered"]), delta=(covid_data["regionData"][0 - 100]["newRecovered"]))