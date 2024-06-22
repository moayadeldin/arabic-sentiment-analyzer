import streamlit as st
from utils.preprocess import preprocessingText
from models.araNet import AraNet
from models.arabert import AraBERT
from models.mazajak import Mazajak

st.sidebar.title("Select Model")

model_option = st.sidebar.selectbox(
    "Choose a model to use for prediction:",
    ("AraNet", "Mazajak", "AraBERT")
)

st.title("Arabic Sentiment Analysis")
user_input = st.text_area(
    "Enter text for Sentiment Analysis:"
)

if st.button("Get Prediction"):

    if user_input:

        preprocessor = preprocessingText(user_input)

        preprocessed_text = preprocessor.cleanText()

        if model_option == "AraNet":

            AraNet = AraNet("models/AraNet_model")

            prediction = AraNet.get_prediction(preprocessed_text)

        elif model_option == "AraBERT":

            AraBERT = AraBERT("models/AraBERT_ASTD_Unbalanced")

            prediction = AraBERT.get_prediction(preprocessed_text)

        elif model_option == "Mazajak":

            prediction = Mazajak.get_prediction(preprocessed_text)

        else:
            raise ValueError("No other models available.")

        st.write(prediction)

    else:
        st.write("Please enter text to analyze.")

