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
    
    temperature = st.sidebar.slider('Temperature (°C)', float(df['Temperature'].min()), float(df['Temperature'].max()), float(df['Temperature'].mean()))
    humidity = st.sidebar.slider('Humidity (%)', float(df['Humidity'].min()), float(df['Humidity'].max()), float(df['Humidity'].mean()))
    windspeed = st.sidebar.slider('Wind Speed (m/s)', float(df['Windspeed'].min()), float(df['Windspeed'].max()), float(df['Windspeed'].mean()))
    solar_radiation = st.sidebar.slider('Solar Radiation (W/m²)', float(df['Solar Radiation'].min()), float(df['Solar Radiation'].max()), float(df['Solar Radiation'].mean()))

    data = {
        'Temperature': temperature,
        'Humidity': humidity,
        'Windspeed': windspeed,
        'Solar Radiation': solar_radiation
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


