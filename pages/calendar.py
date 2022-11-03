import streamlit as st
import requests


d = st.date_input("Enter your date of birth")


st.write('Your birthday is:', d)

val = st.time_input("set timer")
st.write(val)


url= "https://4getmkaykbzgcrbvhgpttlwdaa0yzvyp.lambda-url.us-east-1.on.aws/"
info = requests.get(url)
st.write(info.text)