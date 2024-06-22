from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
from utils.preprocess import preprocessingText

class AraBERT:

    def __init__(self,path_to_model):

        self.path_to_model = path_to_model

        self.tokenizer = AutoTokenizer.from_pretrained(self.path_to_model)

        self.model = AutoModelForSequenceClassification.from_pretrained(self.path_to_model)

    def get_prediction(self,text):

        preprocessor = preprocessingText(text)

        preprocessed_text = preprocessor.cleanText()

        inputs = self.tokenizer(text, return_tensors="pt")

        outputs = self.model(**inputs)

        probs = torch.nn.functional.softmax(outputs.logits, dim=-1)

        label = torch.argmax(probs, dim=-1).item()

        score = probs[0][label].item()

        if label == 0:

            return f"The prediction output for {preprocessed_text} is Positive with {score*100:.2f}% accuracy."

        elif label == 1:

            return f"The prediction output for {preprocessed_text} is Negative with {score*100:.2f}% accuracy."

        elif label == 2:

            return f"The prediction output for {preprocessed_text} is Neutral with {score*100:.2f}% accuracy."

        