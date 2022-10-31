import streamlit as st
import pandas as pd

st.set_page_config(page_title="Health Coach", page_icon=":heart:", layout="wide" )

with st.container():
    st.title ("HealthCoach :heart: :running:")
    st.subheader("hey")

st.sidebar.success("select a page above")