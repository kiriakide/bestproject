import streamlit as st

st.set_page_config(page_title="Assignment1", page_icon=":heart:", layout="wide" )

with st.container():
    st.title ("Application of 6 widgets :heart:")

col1, col2 = st.columns(2)

with col1:
    st.header("_Assignment 1_")
with col2:
    st.header('_Kiriaki Georgiou_')

st.markdown("CEI 521 Advanced Topics in Software Engineering ")

st.sidebar.success("select a widget above")

code = '''def hello():
    print("Hello, Streamlit!")'''
st.code(code, language='python')

