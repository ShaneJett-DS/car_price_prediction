import streamlit as st
import pandas as pd


header = st.container()
dataset = st.container()
features = st.container()
random = st.container()


with header:
    st.title("Car Price Prediction")

with dataset:
    st.header("Test header")
    st.text("Some descriptive text")





st.write("hello, hello")