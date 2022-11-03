import streamlit as st
import calendar

d = st.date_input("Enter your date of birth")


st.write('Your birthday is:', d)

val = st.time_input("set timer")
st.write(val)