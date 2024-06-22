import os
import json
import requests
from utils.preprocess import preprocessingText

class Mazajak:

    def __init__(self):

        self.url = "http://mazajak.inf.ed.ac.uk:8000/api/predict"

    def get_prediction(self,text):

        preprocessor = preprocessingText(text)

        preprocessed_text = preprocessor.cleanText()

        to_sentence = {'data': preprocessed_text}

        data = json.dumps(to_sentence,ensure_ascii=False).encode('utf8')

        headers = {'content-type': 'application/json'}

        try:

            response = requests.post(url=self.url, data=data, headers=headers,timeout=120)

            response.raise_for_status()
            
            prediction = json.loads(response.content)['data']

            return prediction

        except requests.exceptions.Timeout:

            raise TimeoutError('The request timed out after 120 seconds.')

                
        except:

            raise ValueError('An error occured while retrieving the request.')


