import streamlit as st
import requests
from datetime import datetime,timedelta
import pandas as pd

url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'
url_1 = 'https://api.openweathermap.org/data/2.5/onecall/timemachine?lat={}&lon={}&dt={}&appid={}'

def getweather(city):
    result = requests.get(url.format(city))
    if result:
        json = result.json()
        #st.write(json)
        country = json['sys']['country']
        temp = json['main']['temp'] - 273.15
        temp_feels = json['main']['feels_like'] - 273.15
        humid = json['main']['humidity'] - 273.15
        icon = json['weather'][0]['icon']
        lon = json['coord']['lon']
        lat = json['coord']['lat']
        des = json['weather'][0]['description']
        res = [country, round(temp, 1), round(temp_feels, 1),
               humid, lon, lat, icon, des]
        return res, json
    else:
        print("error in search !")

def get_hist_data(lat,lon,start):
    res = requests.get(url_1.format(lat,lon,start))
    data = res.json()
    temp = []
    for hour in data["hourly"]:
        t = hour["temp"]
        temp.append(t)
    return data , temp


st.header('Streamlit Weather Report')
st.markdown('https://openweathermap.org/api')

col1, col2 = st.columns(2)

with col1:
    city_name = st.text_input("Enter a city name")

with col2:
    if city_name:
        res, json = getweather(city_name)

        # st.write(res)
        st.success('Current: ' + str(round(res[1], 2)))
        st.info('Feels Like: ' + str(round(res[2], 2)))
        # st.info('Humidity: ' + str(round(res[3],2)))
        st.subheader('Status: ' + res[7])
        web_str = "![Alt Text]" + "(http://openweathermap.org/img/wn/" + str(res[6]) + "@2x.png)"
        st.markdown(web_str)