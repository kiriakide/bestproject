import streamlit as st
import pandas as pd

st.set_page_config(page_title="Health Coach", page_icon=":heart:", layout="wide" )

with st.container():
    st.title ("Application of 6 widgets :heart:")
    st.caption("hey")

st.sidebar.success("select a page above")
