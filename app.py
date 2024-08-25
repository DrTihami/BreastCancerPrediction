
import streamlit as st
import pandas as pd
import pickle
import warnings

warnings.filterwarnings('ignore')

# Load the model
with open('good_model.pkl', 'rb') as file:
    loaded_model = pickle.load(file)

# Custom CSS
st.markdown("""
<style>
/* General styles */
body {
    font-family: 'Arial', serif;
    background-color: #f0f2f6;
    color: #333;
    margin: 0;
    padding: 0;
}

.container {
    max-width: 1200px;
    margin: auto;
    padding: 20px;
}

.header {
    background-color: #007bff;
    color: white;
    text-align: center;
    padding: 20px;
    border-radius: 10px;
}

.header img {
    display: block;
    margin: 0 auto;
    max-width: 100%;
    height: auto;
}

.header h1 {
    margin-top: 10px;
}

.main-content {
    background-color: #ffffff;
    border-radius: 10px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    padding: 20px;
    margin-top: 20px;
}

h1, h2 {
    color: #333;
    text-align: center;
}

.stButton button {
    background-color: #007bff;
    color: white;
    border: none;
    border-radius: 5px;
    padding: 10px 20px;
    font-size: 16px;
    cursor: pointer;
}

.stButton button:hover {
    background-color: #0056b3;
}

.stSelectbox, .stSlider, .stTextInput {
    margin-bottom: 20px;
}

.stSelectbox select, .stSlider input, .stTextInput input {
    border: 1px solid #ced4da;
    border-radius: 5px;
    padding: 10px;
    font-size: 16px;
    width: 100%;
}

.stSelectbox select:focus, .stSlider input:focus, .stTextInput input:focus {
    border-color: #007bff;
}

</style>
""", unsafe_allow_html=True)

# Main content
st.markdown('<div class="header"><h1>Breast Cancer Prediction Application</h1></div>', unsafe_allow_html=True)

st.write('This App will help you classify whether a patient is suffering from Breast Cancer or not, based on selected parameters')

st.write('Courtesy : Abdul Mohsin Bhat, Senior Data Scientist & Dr. Shabir Ahmad')

st.subheader('Enter the Scan details to know the Status')

# Define input fields
Col1, Col2, Col3 = st.columns(3)
with Col1:
    concave_points_mean = st.number_input('Concave Points Mean', min_value=0.0, max_value=2.0, value=0.094)
with Col2:
    perimeter_worst = st.number_input('Perimeter Worst', min_value=0.0, max_value=300.0, value=128.7)
with Col3:
    texture_worst = st.number_input('Texture Worst', min_value=0.0, max_value=100.0, value=42.79)
Col4, Col5, Col6 = st.columns(3)
with Col4:
    radius_worst = st.number_input('Radius Worst', min_value=0.0, max_value=50.0, value=17.52)
with Col5:
    concavity_worst = st.number_input('Concavity Worst', min_value=0.0, max_value=3.0, value=1.17)
with Col6:
    perimeter_mean = st.number_input('Perimeter Mean', min_value=0.0, max_value=200.0, value=103.0)
Col7, Col8, Col9 = st.columns(3)
with Col7:
    symmetry_worst = st.number_input('Symmetry Worst', min_value=0.0, max_value=1.0, value=0.4089)
with Col8:
    compactness_worst = st.number_input('Compactness Worst', min_value=0.0, max_value=1.5, value=0.7917)
with Col9:
    concave_points_worst = st.number_input('Concave Points Worst', min_value=0.0, max_value=2.0, value=0.2356)
Col10, Col11, Col12, Col13 = st.columns(4)
with Col10:
    perimeter_se = st.number_input('Perimeter SE', min_value=0.0, max_value=5.0, value=2.362)
with Col11:
    area_se = st.number_input('Area SE', min_value=0.0, max_value=50.0, value=22.61)
with Col12:
    concavity_mean = st.number_input('Concavity Mean', min_value=0.0, max_value=1.0, value=0.255)
with Col13:
    symmetry_se = st.number_input('Symmetry SE', min_value=0.0, max_value=1.0, value=0.02137)

# Prepare the input data for prediction
input_data = {
    'concave_points_mean': [concave_points_mean],
    'perimeter_worst': [perimeter_worst],
    'texture_worst': [texture_worst],
    'radius_worst': [radius_worst],
    'concavity_worst': [concavity_worst],
    'perimeter_mean': [perimeter_mean],
    'symmetry_worst': [symmetry_worst],
    'compactness_worst': [compactness_worst],
    'concave_points_worst': [concave_points_worst],
    'perimeter_se': [perimeter_se],
    'area_se': [area_se],
    'concavity_mean': [concavity_mean],
    'symmetry_se': [symmetry_se]
}

# Convert input data to dataframe with important features
input_df = pd.DataFrame(input_data)

# Predict the diagnosis
if st.button('Predict Diagnosis'):
    predicted_diagnosis = loaded_model.predict(input_df)
    result = "Breast Cancer" if predicted_diagnosis[0] == 1 else "No Breast Cancer"
    st.write(f'The patient has: {result}')