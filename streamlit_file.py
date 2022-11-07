import streamlit as st
import pandas as pd


header = st.beta_container()
dataset = st.beta_container()
features = st.beta_container()
random = st.beta_container()


with header:
    st.title("Car Price Prediction")

with dataset:
    st.header("Test header")
    st.text("Some descriptive text")





st.write("hello, hello")