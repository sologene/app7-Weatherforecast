import streamlit as st
import plotly.express as px
from backend import get_data
st.title("Weather forecast for the Next Days")
place = st.text_input("Place: ")
days = st.slider("Forecast days", min_value=1, max_value=5, help = "Select the number of forecasted days")
option = st.selectbox("Select data to view",
                      ("Temprature", "Sky"))
data = get_data(place, days, option)
st.subheader(f"{option} for the next {days} days in {place} ")
figure = px.line(x, y,labels={"x":"Date", "y":"Temprature (C)"})
st.plotly_chart(figure)
