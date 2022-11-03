import streamlit as st
import requests

#PageTitle&sidebar
st.set_page_config(page_title="Calculator", page_icon="🪙", layout="wide" )
st.sidebar.success("select a page above")

#Heading
st.title ("Daily Tasks")
st.caption("This is an interactive widget & was deployed in AWS Function")
st.markdown("Tick as soon as you do a daily task")


#Function
url= "https://qnmv7cfexpjgverograjfduuua0dkkvk.lambda-url.us-east-1.on.aws/?planet="
info = requests.get(url)
st.write(info.text)


#widget
Task1 = st.checkbox('I agree')
Task2 = st.checkbox('I agree')
Task3 = st.checkbox('I agree')

if Task1:
    st.write('Great!')

if Task2:
    st.write('Great!')

if Task3:
    st.write('Great!')