import streamlit as st
import pandas as pd
import pickle

# Load dataset
data = pd.read_csv('solarpowergeneration.csv')

# Sidebar for navigation
st.sidebar.title("Navigation")
options = st.sidebar.radio("Go to", ["EDA", "Prediction"])

# EDA Section
if options == "EDA":
    st.title("Exploratory Data Analysis")
    
    st.write("### Dataset Preview")
    st.dataframe(data.head())

    st.write("### Basic Statistics")
    st.write(data.describe())

    st.write("### Correlation Matrix")
    st.write(data.corr())

# Prediction Section
elif options == "Prediction":
    st.title("Make a Prediction")
    
    # Load the trained model
    with open('gbr.pkl', 'rb') as file:
        model = pickle.load(file)
    
    st.write("### Input Environmental Variables")

    # User inputs for prediction
    distance_to_solar_noon = st.number_input("Distance to Solar Noon", min_value=0.0, max_value=1.0, value=0.5)
    temperature = st.number_input("Temperature", min_value=-50, max_value=150, value=70)
    wind_direction = st.number_input("Wind Direction", min_value=0, max_value=360, value=180)
    wind_speed = st.number_input("Wind Speed", min_value=0.0, max_value=100.0, value=5.0)
    sky_cover = st.number_input("Sky Cover", min_value=0, max_value=100, value=0)
    visibility = st.number_input("Visibility", min_value=0.0, max_value=100.0, value=10.0)
    humidity = st.number_input("Humidity", min_value=0, max_value=100, value=50)
    average_wind_speed = st.number_input("Average Wind Speed (Period)", min_value=0.0, max_value=100.0, value=5.0)
    average_pressure = st.number_input("Average Pressure (Period)", min_value=20.0, max_value=40.0, value=30.0)

    # Make prediction
    prediction = model.predict([[distance_to_solar_noon, temperature, wind_direction, wind_speed,
                                 sky_cover, visibility, humidity, average_wind_speed, average_pressure]])

    st.write(f"### Predicted Power Generated: {prediction[0]:.2f} watts")

