from django.apps import AppConfig
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.text import tokenizer_from_json
import json

class SentimentConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'sentiment'

    # def ready(self):
    #     # Load the sentiment analysis model
    #     global model
    #     model = load_model('E:\\Research_new\\fashion-_frontend\\backend\\sentiment\\models\\model_name_2.h5')
        
    #     # Load the tokenizer
    #     global tokenizer
    #     with open('E:\\Research_new\\fashion-_frontend\\backend\\sentiment\\models\\tokenizer_2.json') as f:
    #         tokenizer_data = json.load(f)
    #         tokenizer = tokenizer_from_json(tokenizer_data)

    #     print("Sentiment analysis model and tokenizer loaded.")
