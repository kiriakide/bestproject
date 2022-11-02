import streamlit as st

st.set_page_config(page_title="Health Coach", page_icon=":heart:", layout="wide" )

with st.container():
    st.title ("Application of 6 widgets :heart:")
    st.subheader("_Assignment 1_")
    st.caption("hey")
    st.markdown('Streamlit is **_really_ cool**.')

st.sidebar.success("select a page above")
