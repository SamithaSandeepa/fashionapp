# sentiment_resources.py
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.text import tokenizer_from_json
import json

_model = None
_tokenizer = None   

def get_model():
    global _model
    if _model is None:
        _model = load_model('E:\\Research_new\\fashion-_frontend\\backend\\sentiment\\models\\model_name_2.h5')
    return _model

def get_tokenizer():
    global _tokenizer
    if _tokenizer is None:
        with open('E:\\Research_new\\fashion-_frontend\\backend\\sentiment\\models\\tokenizer_2.json') as f:
            tokenizer_data = json.load(f)
            _tokenizer = tokenizer_from_json(tokenizer_data)
    return _tokenizer
