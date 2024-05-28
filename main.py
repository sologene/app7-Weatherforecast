import streamlit as st
import plotly.express as px
from backend import get_data
st.title("Weather forecast for the Next Days")
place = st.text_input("Place: ")
days = st.slider("Forecast days", min_value=1, max_value=5, help = "Select the number of forecasted days")
option = st.selectbox("Select data to view",
                      ("Temperature", "Sky"))
try:
    if place:
        st.subheader(f"{option} for the next {days} days in {place} ")
        data = get_data(place, days)
        if option == "Temperature":
            temp = [dit["main"]["temp"] for dit in data]
            temp = [x/10 for x in temp]
            dates = [dit["dt_txt"] for dit in data]
            figure = px.line(x=dates, y=temp,labels={"x":"Date", "y":"Temperature (C)"})
            st.plotly_chart(figure)

        if option == "Sky":
            dates = [dit["dt_txt"] for dit in data]
            images = {"Clear": "images/clear.png","Rain": "images/rain.png", "Clouds": "images/clouds.png", "Snow": "images/snow.png" }
            sky = [dit["weather"][0]["main"] for dit in data]
            img_path = [images[img] for img in sky]
            st.image(img_path, width=200, caption=dates)
except KeyError:
    st.info("You entered a  non-existing place")

