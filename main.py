import streamlit as st

st.set_page_config(page_title="Health Coach", page_icon=":heart:", layout="wide" )

with st.container():
    st.title ("Application of 6 widgets :heart:")

col1, col2 = st.columns(2)

with col1:
    st.subheader("_Assignment 1_")
with col2:
    st.subheader('_Kiriaki Georgiou_')

st.markdown("CEI 521 Advanced Topics in Software Engineering ")

st.sidebar.success("select a widget above")
