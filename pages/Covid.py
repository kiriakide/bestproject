import streamlit as st
import requests

#Headings
st.set_page_config(page_title="Covid Cases", page_icon=":anger:", layout="wide" )

with st.container():
    st.title ("Covid Cases 🦠")
    st.subheader("hey")

st.sidebar.success("select a page above")


#Prostheto to API
url = "https://covid-19-statistics.p.rapidapi.com/reports/total"

querystring = {"date":"2020-04-07"}

headers = {
    "X-RapidAPI-Key": "042e82a4c2msh38a9f638f7c9e75p141557jsn7c288a2c34e7",
    "X-RapidAPI-Host": "covid-19-statistics.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)
covid_data = response.json()
st.write(covid_data)

#Ta vazo sto stremlit
st.metric(label="Last Updated:", value= (covid_data["data"]["last_update"]))

col1,col2,col3 = st.columns(3)

with col1:
    st.metric(label="Deaths", value=(covid_data["data"]["deaths"]), delta="7300")
with col2:
    st.metric(label="Recovered", value=(covid_data["data"]["recovered"]), delta="23539")
with col3:
    st.metric(label="Active", value=(covid_data["data"]["active"]), delta="50156")

