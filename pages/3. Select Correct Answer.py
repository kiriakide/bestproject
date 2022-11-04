import streamlit as st
import requests

#PageTitle&sidebar
st.set_page_config(page_title="Select Correct Answer", page_icon="🪙", layout="wide" )
st.sidebar.success("select a page above")

#Heading
st.title ("Select Correct Answer")
st.caption("This is an interactive widget & was deployed in AWS Function")
st.markdown("Daily Questions to train your brain")


#Widget
genre = st.radio(
    "Question: Which one is a alanet?",
    ('Moon', 'Earth', 'Movie'))


#Function
url= "https://qnmv7cfexpjgverograjfduuua0dkkvk.lambda-url.us-east-1.on.aws/?planet=%s" % (genre)
info = requests.get(url)
st.write(info.text)

code = '''def hello():
    print("Hello, Streamlit!")'''
st.code(code, language='python')

