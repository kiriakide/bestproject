import streamlit as st
import requests

number1 = st.number_input('Insert a number1')
st.write('The current number is ', number1)
number2 = st.number_input('Insert a number2')
st.write('The current number is ', number2)

url1 = "https://gdicyypesekolfiew4kze4i3cy0vylwp.lambda-url.us-east-1.on.aws/?first=%f&second=%f" % (number1, number2)
info = requests.get(url1)
st.write(info.text)