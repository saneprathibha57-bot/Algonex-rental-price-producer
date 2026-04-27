import streamlit as st # used to build the app UI (buttons, inputs, text)
import numpy as np # used to handle numbers (arrays)
import pickle # used to load the trained model


model = pickle.load(open("model.pkl", "rb"))
''' "model.pkl" -> file where your trained model is saved
"rb" -> read binary mode
pickle.load() -> loads the model into memory- > Soo now model is ready to predict '''

st.title("Rental Price Producer")

sqft = st.number_input("Enter Square Feet")
bath = st.number_input("Enter Bathrooms")
bhk = st.number_input("Enter BHK")

if st.button("Predict Price"):
    input_data = np.array([[sqft, bath, bhk]])
    # Model expects input like: [[sqft, bath, bhk]]
    # Example: [[1000, 2, 2]] -> So we convert inputs into NumPy array and reshape it to match the model's expected input format

    prediction = model.predict(input_data)
    st.success(f"Estimated Price: ₹ {prediction[0]:,.2f}") # or st.write("Price:", prediction[0])