# import libraries
import streamlit as st
from joblib import load

# load model from joblib file
model = load('salary_food_model.joblib')

# Create Streamlit Web App
st.title('Salary vs Food Expense Prediction')

# Add Input fields for income
income = st.number_input('Enter your income:')

# Add prediction button
predict_button = st.button('Predict')

# Add prediction logic
if predict_button:
    # Input data into 2D array
    input_data = [[income/1000]]

    # Predict the food expense
    prediction = model.predict(input_data)[0]

    # Display the prediction
    st.write('Prediction food expense:', round(prediction*100, 2), 'THB')