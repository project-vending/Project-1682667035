python
import streamlit as st
import pandas as pd

# Load and display NexRad data
nexrad_df = pd.read_csv('../data/nexrad.csv')
st.write('NexRad Data:')
st.write(nexrad_df)

# Load and display GOES data
goes_df = pd.read_csv('../data/goes.csv')
st.write('GOES Data:')
st.write(goes_df)

# Load and display weather forecast
forecast = {
    'Date': ['2023-03-02', '2023-03-03', '2023-03-04'],
    'Temperature (F)': [58, 61, 63],
    'Precipitation (in)': [0.1, 0.05, 0.0],
    'Cloud Cover (%)': [50, 60, 45]
}
forecast_df = pd.DataFrame(forecast)
st.write('Weather Forecast:')
st.write(forecast_df)
