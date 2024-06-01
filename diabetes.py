import streamlit as st
import pickle
import numpy as np

# Load the trained model
# filename = 'diabetes_dataset.sav'
# with open(filename, 'rb') as file:
#     model_RF = pickle.load(file)
#model_RF = pickle.load(open('diabetes_dataset.sav', 'rb'))

filename1 = 'diabetes_model_1.sav'
filename2 = 'diabetes_model_2.sav'
filename3 = 'diabetes_model_3.sav'

# Load tiga bagian model
with open(filename1, 'rb') as file1:
    RF_model1 = pickle.load(file1)

with open(filename2, 'rb') as file2:
    RF_model2 = pickle.load(file2)

with open(filename3, 'rb') as file3:
    RF_model3 = pickle.load(file3)

# Gabungkan ketiga bagian model menjadi satu model utuh
RF_model = RF_model1 + RF_model2 + RF_model3

# Function to make predictions
def predict_diabetes(features):
    prediction = model_RF.predict([features])
    return prediction[0]


# Streamlit app
st.title("Diabetes Classification App")

st.write("""
Masukkan data pasien untuk mengetahui apakah mereka menderita diabetes atau tidak.
""")

# Input features dictionary
input_features = {
    'RegularMedicine': 'Regular Medicine',
    'Age': 'Age',
    'BMI': 'BMI',
    'Family_Diabetes': 'Family Diabetes',
    'Stress': 'Stress',
    'HighBP': 'HighBP',
    'SoundSleep': 'SoundSleep',
    'PhysicallyActive': 'Physically Active',
    'Sleep': 'Sleep',
    'BPLevel': 'BP Level'
}

# Process input features
features = {}
for key, label in input_features.items():
    features[key] = st.text_input(label)

    # Handle empty inputs
    if features[key] == '':
        features[key] = 0
    else:
        features[key] = float(features[key])

# Collect user input into a feature array
features = np.array([features[key] for key in input_features])

# Prediction
if st.button('Klasifikasi'):
    if any(val == 0.0 for val in features):
        st.warning('Silakan isi semua data sebelum melakukan klasifikasi.')
    else:
        result = predict_diabetes(features)
        if result == 1:
            st.error('Pasien menderita diabetes.')
        else:
            st.success('Pasien tidak menderita diabetes.')
