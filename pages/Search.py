import streamlit as st
from altair import datasets
import datasets
import requests

st.write(""" 
Stocks prices 
""")

st.text_input('Search')

url = "https://covid-19-statistics.p.rapidapi.com/reports/total"

querystring = {"date":"2020-04-07"}

headers = {
	"X-RapidAPI-Key": "042e82a4c2msh38a9f638f7c9e75p141557jsn7c288a2c34e7",
	"X-RapidAPI-Host": "covid-19-statistics.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)

