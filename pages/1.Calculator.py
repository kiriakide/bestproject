import streamlit as st
import requests

#PageTitle&sidebar
st.set_page_config(page_title="Calculator", page_icon="🪙", layout="wide" )
st.sidebar.success("select a page above")

#Heading
st.title ("Calculator")
st.caption("This is an interactive widget & was deployed in AWS Function")
st.markdown("Give two numbers and get the result of the addition")


st.header("Insert 2 Numbers")

#InsertNumbers
number1 = st.number_input('Insert a number1')
st.write('The current number is ', number1)
number2 = st.number_input('Insert a number2')
st.write('The current number is ', number2)

#Resultfromfunction
url1 = "https://gdicyypesekolfiew4kze4i3cy0vylwp.lambda-url.us-east-1.on.aws/?first=%f&second=%f" % (number1, number2)
info = requests.get(url1)
st.write(info.text)

code = '''import streamlit as st
import requests

#PageTitle&sidebar
st.set_page_config(page_title="Calculator", page_icon="🪙", layout="wide" )
st.sidebar.success("select a page above")

#Heading
st.title ("Calculator")
st.caption("This is an interactive widget & was deployed in AWS Function")
st.markdown("Give two numbers and get the result of the addition")


st.header("Insert 2 Numbers")

#InsertNumbers
number1 = st.number_input('Insert a number1')
st.write('The current number is ', number1)
number2 = st.number_input('Insert a number2')
st.write('The current number is ', number2)

#Resultfromfunction
url1 = "https://gdicyypesekolfiew4kze4i3cy0vylwp.lambda-url.us-east-1.on.aws/?first=%f&second=%f" % (number1, number2)
info = requests.get(url1)
st.write(info.text)'''
st.code(code, language='python')


code = '''import json

def lambda_handler(event, context):

    param = event["queryStringParameters"]
    
    #down
    num1 = float(param["first"])
    num2 = float(param["second"])
    num=num1+num2
    return_f=f"result: {num}"
    #up
    return {
        'statusCode': 200,
        'body': f'{return_f}',
        'headers': { 'Content-Type': "text/html" }
    }'''
st.code(code, language='python')