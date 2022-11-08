import streamlit as st
import pandas as pd
import os



cwd = os.getcwd()


# Create containers for Web Application
header = st.container()
dataset = st.container()
eda_1 = st.container()
eda_2 = st.container()
eda_3 = st.container()
eda_4 = st.container()
eda_5 = st.container()
random = st.container()


with header:
    st.title("Car Price Prediction")

with dataset:
    st.header("The Dataset")
    st.text("Some descriptive text")
    data = pd.read_csv(cwd + "/Car_Price_Pred.csv")
    st.dataframe(data.head())

with eda_1:
    # Create make column using CarName variable
    # Find the count of make
    data["Make"] = data["CarName"].str.split(" ").str[0]
    top_10_make = pd.Series(data["Make"].value_counts().head(n=10))
    top_10_make = top_10_make.sort_values(ascending=False)
    top_10_make_perc = pd.Series(data["Make"].value_counts(normalize=True).head(n=10))

    st.title("Top 10 Makes in Dataset")
    st.bar_chart(top_10_make)

   

with eda_2:



st.write("End")