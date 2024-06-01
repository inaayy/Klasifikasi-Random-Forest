# import streamlit as st
# import pickle
# import numpy as np

# # Load the trained model
# # filename = 'diabetes_dataset.sav'
# # with open(filename, 'rb') as file:
#     # model = pickle.load(file)
# model_RF = pickle.load(open('diabetes_dataset.sav', 'rb'))

# # Function to make predictions
# def predict_diabetes(features):
#     prediction = model_RF.predict([features])
#     return prediction[0]


# # Streamlit app
# st.title("Diabetes Classification App")

# st.write("""
# Masukkan data pasien untuk mengetahui apakah mereka menderita diabetes atau tidak.
# """)

# # Input features dictionary
# input_features = {
#     'RegularMedicine': 'Regular Medicine',
#     'Age': 'Age',
#     'BMI': 'BMI',
#     'Family_Diabetes': 'Family Diabetes',
#     'Stress': 'Stress',
#     'HighBP': 'HighBP',
#     'SoundSleep': 'SoundSleep',
#     'PhysicallyActive': 'Physically Active',
#     'Sleep': 'Sleep',
#     'BPLevel': 'BP Level'
# }

# # Process input features
# features = {}
# for key, label in input_features.items():
#     features[key] = st.text_input(label)

#     # Handle empty inputs
#     if features[key] == '':
#         features[key] = 0
#     elif key in ['Age', 'BMI', 'SoundSleep', 'Sleep']:
#         features[key] = float(features[key])

# # Collect user input into a feature array
# features = np.array([features[key] for key in input_features])

# # Prediction
# if st.button('Klasifikasi'):
#     result = predict_diabetes(features)
#     if result == 1:
#         st.error('Pasien menderita diabetes.')
#     else:
#         st.success('Pasien tidak menderita diabetes.')


import pickle
import numpy as np
import streamlit as st

# load save model
model_RF = pickle.load(open('diabetes_dataset.sav','rb'))

# judul web
st.title('Klasifikasi Penyakit Diabetes')

col1, col2, col3 = st.columns(3)

with col1:
    RegularMedicine = st.number_input('Regular Medicine')
with col2:
    Age = st.number_input('Age')
with col3:
    BMI = st.number_input('BMI')
with col1:
    Family_Diabetes = st.number_input('Family Diabetes')
with col2:
    Stress = st.number_input('Stress')
with col3:
    HighBP = st.number_input('HighBP')
with col1:
    SoundSleep = st.number_input('SoundSleep')
with col2:
    PhysicallyActive = st.number_input('Physically Active')
with col3:
    Sleep = st.number_input('Sleep')
with col1:
    BPLevel = st.number_input('BPLevel')


# code for prediction
diabetes_diagnosis =''

# membuat tombol prediksi
if st.button('Klasifikasi Penyakit Diabetes'):
    if all(val == 0 for val in [RegularMedicine, Age, BMI, Family_Diabetes, Stress, HighBP, SoundSleep, PhysicallyActive, Sleep, BPLevel]):
        diabetes_diagnosis = 'Data Belum Terisi'
    else:
        diabetes_prediction = model_RF.predict([[RegularMedicine, Age, BMI, Family_Diabetes, Stress, HighBP, SoundSleep, PhysicallyActive, Sleep, BPLevel]])

        if diabetes_prediction[0] == 1:
            diabetes_diagnosis = 'Pasien Diabetes'
        else:
            diabetes_diagnosis = 'Pasien Tidak DIabetes'
st.success(diabetes_diagnosis)
