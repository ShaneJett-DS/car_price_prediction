import streamlit as st
import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px


cwd = os.getcwd()


# Create containers for Web Application
header = st.container()
dataset = st.container()
eda_1 = st.container()
eda_2 = st.container()
eda_3 = st.container()
eda_4 = st.container()
eda_5 = st.container()
model = st.container()
END = st.container()
random = st.container()


with header:
    st.title("Car Price Prediction")

with dataset:
    st.header("The Dataset")
    st.text("Describe the Dataset")
    st.text("Describe the goal of the Project")
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
    st.title("Separate the data into two Categories to compare thier linear relationship:")
    st.text("1. Engine Data")
    st.text("2. Chassis/Body Data")

    # Create two dataframes: 1) Variables with chassis data + target
    #                        2) Variables with engine data + target
    body_data = data[["price", "wheelbase", "carlength", "carwidth", "carheight", "curbweight"]]
    engine_data = data[["price", "enginesize", "boreratio", "stroke", "compressionratio", "horsepower", "citympg", "highwaympg", "peakrpm"]]

    # Display a correlation matix for each of the dataframes
    st.header("3. Create Correlation Matrices")
    body_corr = body_data.corr()
    eng_corr = engine_data.corr()
    heat_fig = sns.heatmap(body_corr)

    st.subheader("Body data Correlation Matrix")
    st.table(body_corr)
  
    
    fig, ax = plt.subplots(figsize=(12,8))
    sns.heatmap(body_corr, cmap="Blues", annot=True)
    plt.title("Body Data vs Price Correlation Heatmap", fontsize=20)
    st.pyplot(fig)

    st.subheader("Engine data Correlation Matrix")
    st.table(eng_corr)

    fig2, ax2 = plt.subplots(figsize=(12,8))
    sns.heatmap(eng_corr, cmap="Blues", annot=True)
    plt.title("Body Data vs Price Correlation Heatmap", fontsize=20)
    st.pyplot(fig2)

with eda_3:
    st.header("Analyze the linear relationships")
    st.text("Some description of the method and goals of the analysis")

    st.subheader("Body Variables vs Price")
    fig1 = px.scatter(body_data, x="price", y="curbweight", title="Curb Weight vs Price", trendline="ols")
    st.plotly_chart(fig1)    
    
    fig2 = px.scatter(body_data, x="price", y="carwidth", title="Car Width vs Price", trendline="ols")
    st.plotly_chart(fig2)
    
    st.subheader("Engine Variables vs Price")
    fig1a = px.scatter(engine_data, x="price", y="enginesize", title="Engine Size vs Price", trendline="ols")
    st.plotly_chart(fig1a) 

    fig2a = px.scatter(engine_data, x="price", y="horsepower", title="Horsepower vs Price", trendline="ols")
    st.plotly_chart(fig2a)   

with model:
    st.header("Linear Regression Analysis")
    st.subheader("Linear Regression Model")

    st.subheader("RidgeCV Regression Model")

    st.subheader("ElasticNetCV Model")

    st.subheader("LassoCV Model")

    st.subheader("BayesianRidgeCV Model")

    st.subheader("SGDRegressor Model")


with END:

    st.write("End")