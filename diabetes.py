import streamlit as st
import pickle
import numpy as np

# Load the trained model
filename = 'diabetes_dataset.sav'
with open(filename, 'rb') as file:
    model = pickle.load(file)

# Function to make predictions
def classification_diabetes(features):
    classification = model.predict([features])
    return classification[0]

# Streamlit app
st.title("Diabetes Classification App")

st.write("""
# Prediksi Diabetes
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
cols = st.columns(3)
features = {}
all_filled = True

with st.form("input_form"):
    for idx, (key, label) in enumerate(input_features.items()):
        with cols[idx % 3]:  # Alternate between columns
            features[key] = st.text_input(label)

    # Handle empty inputs
    if features[key] == '':
        all_filled = False  # Set flag to False if any input is empty
    else:
        # Convert specific inputs to float
        if key in ['Age', 'BMI', 'SoundSleep', 'Sleep']:
            try:
                features[key] = float(features[key])
            except ValueError:
                st.warning(f'{label} harus berupa angka.')
                all_filled = False

    # Submit button for the form
    submitted = st.form_submit_button("Klasifikasi")
    
# Collect user input into a feature array
features_array = np.array([features[key] for key in input_features])

# Klasifikasi
if submitted:
    if all_filled:
        result = classification_diabetes(features_array)
        if result == 1:
            st.error('Pasien menderita diabetes.')
        else:
            st.success('Pasien tidak menderita diabetes.')
    else:    
        st.warning('Silakan isi semua data sebelum melakukan prediksi.')
