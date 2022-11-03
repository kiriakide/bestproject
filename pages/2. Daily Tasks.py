import streamlit as st
import requests


url= "https://qnmv7cfexpjgverograjfduuua0dkkvk.lambda-url.us-east-1.on.aws/?planet="
info = requests.get(url)
st.write(info.text)

option = st.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone'))

st.write('You selected:', option)