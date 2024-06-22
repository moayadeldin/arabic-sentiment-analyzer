from aranet import aranet
from utils.preprocess import preprocessingText

class AraNet:

    def __init__(self, path_to_model):

        self.path_to_model = path_to_model

        self.model = aranet.AraNet(path_to_model)

    
    def get_prediction(self,text):
        
        preprocessor = preprocessingText(text)

        preprocessed_text = preprocessor.cleanText()

        prediction = self.model.predict(text=preprocessed_text)

        if prediction[0][0] == 'pos':

            return f"The prediction output for {preprocessed_text} is Positive with {prediction[0][1]*100:.2f}% accuracy."

        elif prediction[0][1] == 'neg':
         
            return f"The prediction output for {preprocessed_text} is Negative with {prediction[0][1]*100:.2f} % accuracy."

        else:
            raise ValueError('The model gives only binary predictions.')


    
        