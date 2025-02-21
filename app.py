import streamlit as st
import pickle
import numpy as np
import pandas as pd

# Load the pre-trained model and preprocessor
model = pickle.load(open('notebooks/best_model.pkl', 'rb'))
preprocessor = pickle.load(open('notebooks/preprocessor.pkl', 'rb'))

# Page Config
st.set_page_config(page_title="Car Price Prediction", page_icon="🚗", layout="wide")

# Custom Styling
st.markdown(
    """
    <style>
    .main {background-color: #e3f2fd;}
    .stButton>button {background-color: #1e88e5; color: white; font-size: 18px; border-radius: 10px;}
    .stTitle {color: #0d47a1; text-align: center;}
    .stMarkdown {color: #1565c0;}
    .stSelectbox>div {background-color: #bbdefb; border-radius: 5px;}
    .stNumberInput>div>input {background-color: #e3f2fd; border-radius: 5px;}
    </style>
    """,
    unsafe_allow_html=True
)

# App Title
st.title("🚗 Car Price Prediction")
st.markdown("### Enter car details below to predict the price")

# Layout
col1, col2 = st.columns(2)

with col1:
    symboling = st.number_input('Symboling', min_value=-3, max_value=3)
    fueltype = st.selectbox('Fuel Type', ['gas', 'diesel'])
    aspiration = st.selectbox('Aspiration', ['std', 'turbo'])
    doornumber = st.selectbox('Number of Doors', ['two', 'four'])
    carbody = st.selectbox('Car Body Type', ['hardtop', 'wagon', 'sedan', 'hatchback', 'convertible'])
    drivewheel = st.selectbox('Drive Wheel Type', ['rwd', 'fwd', '4wd'])
    enginelocation = st.selectbox('Engine Location', ['front', 'rear'])
    wheelbase = st.number_input('Wheelbase (in)', min_value=80.0, max_value=130.0, step=0.1)
    carlength = st.number_input('Car Length (in)', min_value=140.0, max_value=200.0, step=0.1)
    carwidth = st.number_input('Car Width (in)', min_value=60.0, max_value=80.0, step=0.1)
    carheight = st.number_input('Car Height (in)', min_value=50.0, max_value=70.0, step=0.1)

with col2:
    curbweight = st.number_input('Curb Weight (lbs)', min_value=1500, max_value=4000, step=10)
    enginetype = st.selectbox('Engine Type', ['dohc', 'ohc', 'l', 'rotor', 'ohcf', 'dohcv'])
    cylindernumber = st.number_input('Number of Cylinders', min_value=3, max_value=12)
    enginesize = st.number_input('Engine Size (cc)', min_value=60, max_value=500, step=10)
    fuelsystem = st.selectbox('Fuel System', ['mpfi', '2bbl', '1bbl', 'spdi', '4bbl', 'mfi'])
    boreratio = st.number_input('Bore Ratio', min_value=2.0, max_value=4.0, step=0.1)
    stroke = st.number_input('Stroke', min_value=2.0, max_value=4.0, step=0.1)
    compressionratio = st.number_input('Compression Ratio', min_value=7.0, max_value=12.0, step=0.1)
    horsepower = st.number_input('Horsepower', min_value=50, max_value=300, step=10)
    peakrpm = st.number_input('Peak RPM', min_value=4000, max_value=8000, step=100)
    citympg = st.number_input('City MPG', min_value=10, max_value=50, step=1)
    highwaympg = st.number_input('Highway MPG', min_value=10, max_value=50, step=1)

# Prepare input data
data = pd.DataFrame([[symboling, fueltype, aspiration, doornumber, carbody, drivewheel, enginelocation, wheelbase,
                      carlength, carwidth, carheight, curbweight, enginetype, cylindernumber, enginesize,
                      fuelsystem, boreratio, stroke, compressionratio, horsepower, peakrpm, citympg, highwaympg]],
                    columns=['symboling', 'fueltype', 'aspiration', 'doornumber', 'carbody', 'drivewheel',
                             'enginelocation', 'wheelbase', 'carlength', 'carwidth', 'carheight', 'curbweight',
                             'enginetype', 'cylindernumber', 'enginesize', 'fuelsystem', 'boreratio', 'stroke',
                             'compressionratio', 'horsepower', 'peakrpm', 'citympg', 'highwaympg'])

# Convert 'doornumber' from string to numeric
data['doornumber'] = data['doornumber'].map({'two': 2, 'four': 4})

# Predict Button
if st.button("🔍 Predict Price"):
    try:
        transformed_data = preprocessor.transform(data)
        prediction = model.predict(transformed_data)
        st.success(f'🚘 Estimated Car Price: **${prediction[0]:,.2f}**')
    except Exception as e:
        st.error(f"⚠️ An error occurred: {e}")
