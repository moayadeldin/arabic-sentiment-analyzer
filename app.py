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

folder_path = None
if model_option in ["AraNet", "AraBERT"]:

    folder_path = st.sidebar.text_input("Enter model's folder path")

st.title("Arabic Sentiment Analysis")
user_input = st.text_area(
    "Enter text for Sentiment Analysis:"
)

if st.button("Get Prediction"):

    if user_input and (folder_path or model_option == "Mazajak"):

        preprocessor = preprocessingText(user_input)

        preprocessed_text = preprocessor.cleanText()

        if model_option == "AraNet":

            AraNet = AraNet(folder_path)

            prediction = AraNet.get_prediction(preprocessed_text)

        elif model_option == "AraBERT":

            AraBERT = AraBERT(folder_path)

            prediction = AraBERT.get_prediction(preprocessed_text)

        elif model_option == "Mazajak":

            prediction = Mazajak.get_prediction(preprocessed_text)

        else:
            raise ValueError("No other models available.")

        st.write(prediction)

    else:
        st.write("Please enter text to analyze.")

