import streamlit as st
import requests

st.write(""" 
Covid Update
""")

url = "https://covid-19-statistics.p.rapidapi.com/reports/total"

querystring = {"date":"2020-04-07"}

headers = {
	"X-RapidAPI-Key": "042e82a4c2msh38a9f638f7c9e75p141557jsn7c288a2c34e7",
	"X-RapidAPI-Host": "covid-19-statistics.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)
covid_data = response.json()
st.write(covid_data)

try:

col1, col2, col3 = st.columns(3)
col1.metric("Temperature", "70 °F", "1.2 °F")
col2.metric("Wind", "9 mph", "-8%")
col3.metric("Humidity", "86%", "4%")
