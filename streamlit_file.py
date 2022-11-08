import streamlit as st
import pandas as pd
import os

cwd = os.getcwd()

header = st.container()
dataset = st.container()
features = st.container()
random = st.container()


with header:
    st.title("Car Price Prediction")

with dataset:
    st.header("Test header")
    st.text("Some descriptive text")
    data = pd.read_csv(cwd + "/Car_Price_Pred.csv")
    st.dataframe(data.head(n=10))





st.write("End")