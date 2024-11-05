import streamlit as st
import pickle
import numpy as np
from sklearn.preprocessing import StandardScaler

# Title of the app
st.title("Predict survival on the Titanic")

@st.dialog("Predict survival on the Titanic")
def predict():
    # Display input parameters
    st.write("Input Parameters:")
    st.write(f"Passenger ID: {passenger_id}")
    st.write(f"Passenger Class: {passenger_class}")
    st.write(f"Name: {name}")
    st.write(f"Sex: {sex}")
    st.write(f"Age: {age}")
    st.write(f"Siblings/Spouses Aboard: {sibling_spouse}")
    st.write(f"Parents/Children Aboard: {parent_child}")
    st.write(f"Ticket: {ticket}")
    st.write(f"Fare: {fare}")
    st.write(f"Cabin: {cabin}")
    sex_numeric = 0
    if sex == 'Male':
        sex_numeric = 1
    else:
        sex_numeric = 0
    input_data = np.array([[passenger_class, sex_numeric, age, sibling_spouse, parent_child, fare]])
    
    

    # Load the trained model from the pickle file
    with open('model/model.pkl', 'rb') as f:
        model = pickle.load(f)

    # Use the loaded model to predict the FWI
    prediction = model.predict(input_data)
    st.write(f"Predicted Survival Chance: {prediction[0]:.2f}")


# Passenger ID: Numerical input
passenger_id = st.number_input('Passenger ID', min_value=1, value=1, step=1)

# Passenger Class: Select from 1 to 3
passenger_class = st.selectbox('Passenger Class', options=[1, 2, 3])

# Name: Text input for alphabetical names
name = st.text_input('Name')

# Sex: Radio button for selecting male or female
sex = st.radio('Sex', options=['Male', 'Female'])

# Age: Numerical input between 0 and 100
age = st.number_input('Age', min_value=0, max_value=100, value=30, step=1)

# Sibling or Spouse: Numerical input for the count
sibling_spouse = st.number_input('Sibling or Spouse', min_value=0, value=0, step=1)

# Parent or Child: Numerical input for the count
parent_child = st.number_input('Parent or Child', min_value=0, value=0, step=1)

# Ticket: Text input for ticket information
ticket = st.text_input('Ticket')

# Fare: Numerical input for the fare
fare = st.number_input('Fare', min_value=0.0, value=0.0, step=0.1)

# Cabin: Text input for cabin information
cabin = st.text_input('Cabin')



# Check if any input is missing
inputs_filled = all([
    passenger_id is not None,
    passenger_class is not None,
    name is not None,
    sex is not None,
    age is not None,
    sibling_spouse is not None,
    parent_child is not None,
    ticket is not None,
    fare is not None,
    cabin is not None,
])

# Button to submit the form
if st.button('Predict Survival Chances.', disabled=not inputs_filled):
    predict()

# Display a message if the button is inactive
if not inputs_filled:
    st.write("Please fill out all the inputs to enable the prediction.")
