import streamlit as st
import calendar

c = calendar.TextCalendar(calendar.SUNDAY)
ok = c.formatmonth(2025,1)

st.write(ok)