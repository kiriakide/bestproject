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
url= "https://df3ajmtjofdu34xvb2mp3y33ce0wtwii.lambda-url.us-east-1.on.aws/?list=" %()
info = requests.get(url)
st.write(info.text)


#widget
Task1 = st.checkbox('Groceries')
Task2 = st.checkbox('Gym')
Task3 = st.checkbox('Read')
tasks=Task1+Task2+Task3
st.write(tasks)
if Task1:
    st.write('Great!')

if Task2:
    st.write('Great!')

if Task3:
    st.write('Great!')