import streamlit as st
import requests

# Headings
st.set_page_config(page_title="Weather", page_icon=":sunny:", layout="wide")

with st.container():
    st.title(":snowflake: :umbrella: Weather Indicator :sunny: :cloud:")
    st.caption("This is an interactive widget & retrieved data from **Open weather Website**")
    st.markdown("Give the city to find out about the weather there")

st.sidebar.success("select a page above")

#API
API_KEY = "fbe6ba32126407a59e4d8367af7405be"

def find_current_weather(city):
    base_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
    weather_data = requests.get(base_url).json()
    st.write(weather_data)

def convert_to_celcius(temperature_in_kelvin):
    return temperature_in_kelvin - 273.15


    try:
        weather = weather_data['weather'][0]['main']
        icon_id = weather_data['weather'][0]['icon']
        temperature = round(convert_to_celcius(weather_data['main']['temp']))
        icon = f"http://openweathermap.org/img/wn/{icon_id}@2x.png"
    except KeyError:
        st.error("City Not Found")
        st.stop()
    return weather, temperature, icon

st.header("Search here about the weather")

def main():
    city = st.text_input("Enter the City").lower()
    if st.button("How's the weather?"):
        weather, temperature, icon = find_current_weather(city)
        col_1, col_2 = st.columns(2)
        with col_1:
            st.metric(label="Temperature", value=f"{temperature}°C")
        with col_2:
            st.write(weather)
            st.write(temperature)
            st.image(icon)


if __name__ == '__main__':
    main()
