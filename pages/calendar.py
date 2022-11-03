import streamlit as st
import calendar

c = calendar.TextCalendar(calendar.SUNDAY)
ok = c.formatmonth(2025,1)

st.write(ok)

#adding a date input widget

d = st.date_input("Enter your date of birth")



#displaying the date entered by the user

st.write('Your birthday is:', d)
