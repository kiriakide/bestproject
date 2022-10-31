import streamlit as st
from PIL import Image
import pandas as pd
import base64
import requests
import json
import time

image = Image.open('logo.jpg')

st.image(image, width = 500)

st.title('Crypto Price App')
st.markdown("""
This app retrieves cryptocurrency prices for the top 100 cryptocurrency from the **CoinMarketCap**!
""")