import streamlit as st
import pandas as pd
import os
import plotly.express as px

cwd = os.getcwd()


# Create containers for Web Application
header = st.container()
dataset = st.container()
eda = st.container()
random = st.container()


with header:
    st.title("Car Price Prediction")

with dataset:
    st.header("The Dataset")
    st.text("Some descriptive text")
    data = pd.read_csv(cwd + "/Car_Price_Pred.csv")
    st.dataframe(data.head())

with eda:
    # Create make column using CarName variable
    # Find the count of make
    data["Make"] = data["CarName"].str.split(" ").str[0]
    top_10_make = pd.Series(data["Make"].value_counts().head(n=10))
    top_10_make_perc = pd.Series(data["Make"].value_counts(normalize=True).head(n=10))


    st.table(px.bar(top_10_make))


    st.table(px.bar(top_10_make_perc))




st.write("End")