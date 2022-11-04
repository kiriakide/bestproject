import streamlit as st
import requests

#PageTitle&sidebar
st.set_page_config(page_title="Calculator", page_icon="🪙", layout="wide" )
st.sidebar.success("select a page above")

#Heading
st.title ("Daily Tasks")
st.caption("This is an interactive widget & was deployed in AWS Function")
st.markdown("Tick as soon as you do a daily task")


#widget
Task1 = st.checkbox('Groceries')
Task2 = st.checkbox('Gym')
Task3 = st.checkbox('Read')
tasks=""
if Task1:
    if tasks == "":
        tasks= tasks+"Groceries"
    else:
        tasks=tasks+"_Groceries"
if Task2:
    if tasks == "":
        tasks= tasks+"Gym"
    else:
        tasks=tasks+"_Gym"
if Task3:
    if tasks == "":
        tasks= tasks+"Read"
    else:
        tasks=tasks+"_Read"

#Function
url= "https://df3ajmtjofdu34xvb2mp3y33ce0wtwii.lambda-url.us-east-1.on.aws/?list=" %(tasks)
info = requests.get(url)
st.write(info.text)