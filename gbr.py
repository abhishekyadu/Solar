import streamlit as st
import pandas as pd
import numpy as np
import pickle


    
with open('gbr.pkl', 'rb') as file:
    model = pickle.load(file)
    
df = pd.read_csv('solarpowergeneration.csv')


# Title and Description
st.title("Solar Power Generation Prediction")
st.write("This app predicts solar power generation based on environmental variables.")

# Sidebar for User Input
st.sidebar.header("User Input Parameters")

def user_input_features():
    
    temperature = st.sidebar.slider('temperature (°C)', float(df['temperature'].min()), float(df['temperature'].max()), float(df['temperature'].mean()))
    humidity = st.sidebar.slider('humidity (%)', float(df['humidity'].min()), float(df['humidity'].max()), float(df['humidity'].mean()))
    wind-speed = st.sidebar.slider('wind-speed (m/s)', float(df['wind-speed'].min()), float(df['wind-speed'].max()), float(df['wind-speed'].mean()))
    solar_radiation = st.sidebar.slider('solar Radiation (W/m²)', float(df['solar Radiation'].min()), float(df['solar Radiation'].max()), float(df['solar Radiation'].mean()))

    data = {
        'temperature': temperature,
        'humidity': humidity,
        'windspeed': windspeed,
        'solar Radiation': solar_radiation
    }
    features = pd.DataFrame(data, index=[0])
    return features

input_df = user_input_features()


# Display user input
st.subheader('User Input Parameters')
st.write(input_df)

# Make Predictions
prediction = model.predict(input_df)

# Display Predictions
st.subheader('Predicted Solar Power Generation (kW)')
st.write(prediction)

# Show a Sample of the Data (Optional)
st.subheader('Sample Data from Dataset')
st.write(df.head())


