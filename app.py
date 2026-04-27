import streamlit as st # used to build the app UI (buttons, inputs, text)
import numpy as np # used to handle numbers (arrays)
import joblib # used to load the trained model
import os # used to check if file exists

# Check if model.pkl exists
if not os.path.exists("model.pkl"):
    st.error("The model file 'model.pkl' is missing. Please ensure it is in the project directory.")
    st.stop()

try:
    model = joblib.load("model.pkl")
except Exception as e:
    st.error(f"Failed to load the model: {e}")
    st.stop()

''' "model.pkl" -> file where your trained model is saved
"rb" -> read binary mode
pickle.load() -> loads the model into memory- > Soo now model is ready to predict '''

st.title("Rental Price Producer")
'''location = st.selectbox(
    "Select Location",
    [
        "Bellandur",
        "Bommanahalli",
        "Brookefield",
        "Electronic City",
        "Krishnarajapura"
    ]
)'''


sqft = st.number_input("Enter Square Feet")

'''sqft = st.number_input(
    "Enter Square Feet",
    min_value=300,
    max_value=10000,
    value=1000
)'''

bath = st.number_input("Enter Bathrooms")

bhk = st.number_input("Enter BHK")

''' bath = st.selectbox(
    "Select Bathrooms",
    [1, 2, 3, 4, 5]
)

bhk = st.selectbox(
    "Select BHK",
    [1, 2, 3, 4, 5]
)'''

if st.button("Predict Price"):
    try:
        input_data = np.array([[sqft, bath, bhk]])
        # Model expects input like: [[sqft, bath, bhk]]
        # Example: [[1000, 2, 2]] -> So we convert inputs into NumPy array and reshape it to match the model's expected input format


        '''input_data = pd.DataFrame([{
        "sqft": sqft,
        "bath": bath,
        "bhk": bhk,
        "location": location
        }])
        input_data = pd.get_dummies(input_data) '''
        
        '''input_data = input_data.reindex(
        columns=X.columns,
        fill_value=0
        )'''

        prediction = model.predict(input_data)
        st.success(f"Estimated Price: ₹ {prediction[0]:,.2f}") # or st.write("Price:", prediction[0])
    except Exception as e:
        st.error(f"Prediction failed: {e}")
