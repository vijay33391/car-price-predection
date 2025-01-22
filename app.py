import streamlit as st
import pickle
import numpy as np
import pandas as pd
import sys  # Import sys to avoid NameError if it's needed in preprocessor or model

# Load the pre-trained model and preprocessor
model = pickle.load(open('D:\\portifilo\\end_to_end\\ml\simple_projects\\simple car_price_predict\\notebooks\\best_model.pkl', 'rb'))
preprocessor = pickle.load(open('D:\\portifilo\\end_to_end\ml\\simple_projects\\simple car_price_predict\\notebooks\\preprocessor.pkl', 'rb'))

# Set the title of the app
st.title('Car Price Prediction')

# User input fields
symboling = st.number_input('Symboling', min_value=-3, max_value=3)
fueltype = st.selectbox('Fuel Type', ['gas', 'diesel'])
aspiration = st.selectbox('Aspiration', ['std', 'turbo'])
doornumber = st.selectbox('Number of Doors', ['two', 'four'])
carbody = st.selectbox('Car Body Type', ['hardtop', 'wagon', 'sedan', 'hatchback', 'convertible'])
drivewheel = st.selectbox('Drive Wheel Type', ['rwd', 'fwd', '4wd'])
enginelocation = st.selectbox('Engine Location', ['front', 'rear'])
wheelbase = st.number_input('Wheelbase', min_value=80.0, max_value=130.0, step=0.1)
carlength = st.number_input('Car Length', min_value=140.0, max_value=200.0, step=0.1)
carwidth = st.number_input('Car Width', min_value=60.0, max_value=80.0, step=0.1)
carheight = st.number_input('Car Height', min_value=50.0, max_value=70.0, step=0.1)
curbweight = st.number_input('Curb Weight', min_value=1500, max_value=4000, step=10)
enginetype = st.selectbox('Engine Type', ['dohc', 'ohc', 'l', 'rotor', 'ohcf', 'dohcv'])
cylindernumber = st.number_input('Number of Cylinders', min_value=3, max_value=12)
enginesize = st.number_input('Engine Size', min_value=60, max_value=500, step=10)
fuelsystem = st.selectbox('Fuel System', ['mpfi', '2bbl', '1bbl', 'spdi', '4bbl', 'mfi'])
boreratio = st.number_input('Bore Ratio', min_value=2.0, max_value=4.0, step=0.1)
stroke = st.number_input('Stroke', min_value=2.0, max_value=4.0, step=0.1)
compressionratio = st.number_input('Compression Ratio', min_value=7.0, max_value=12.0, step=0.1)
horsepower = st.number_input('Horsepower', min_value=50, max_value=300, step=10)
peakrpm = st.number_input('Peak RPM', min_value=4000, max_value=8000, step=100)
citympg = st.number_input('City MPG', min_value=10, max_value=50, step=1)
highwaympg = st.number_input('Highway MPG', min_value=10, max_value=50, step=1)

# Input data
input_data = pd.DataFrame([[symboling, fueltype, aspiration, doornumber, carbody, drivewheel, enginelocation, wheelbase,
                            carlength, carwidth, carheight, curbweight, enginetype, cylindernumber, enginesize,
                            fuelsystem, boreratio, stroke, compressionratio, horsepower, peakrpm, citympg, highwaympg]],
                          columns=['symboling', 'fueltype', 'aspiration', 'doornumber', 'carbody', 'drivewheel',
                                   'enginelocation', 'wheelbase', 'carlength', 'carwidth', 'carheight', 'curbweight',
                                   'enginetype', 'cylindernumber', 'enginesize', 'fuelsystem', 'boreratio', 'stroke',
                                   'compressionratio', 'horsepower', 'peakrpm', 'citympg', 'highwaympg'])
# Map the 'doornumber' feature from string to numeric
input_data['doornumber'] = input_data['doornumber'].map({'two': 2, 'four': 4})


# Predict button
if st.button('Predict'):
    try:
        # Transform and predict
        transformed_data = preprocessor.transform(input_data)
        prediction = model.predict(transformed_data)
        st.write(f'Predicted Value: {prediction[0]}')
    except Exception as e:
        st.error(f"An error occurred: {e}")
