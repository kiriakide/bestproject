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

code = '''import streamlit as st
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
st.write(info.text)'''
st.code(code, language='python')

code = '''import json

def lambda_handler(event, context):

    param = event["queryStringParameters"]
    
    #down
    text_check = param['planet']
    if(text_check=='Earth'):
        return_f =f"Correct Answer"
    else:
        return_f =f"Wrong answer"

    #up
    return {
        'statusCode': 200,
        'body': f'{return_f}',
        'headers': { 'Content-Type': "text/html" }
    }'''
st.code(code, language='python')