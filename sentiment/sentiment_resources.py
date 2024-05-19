# sentiment_resources.py
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.text import tokenizer_from_json
import json
import os
from django.conf import settings

_model = None
_tokenizer = None   

def get_model():
    global _model
    if _model is None:
        model_path = os.path.join(settings.BASE_DIR, 'sentiment', 'models', 'model_name_2.h5')
        _model = load_model(model_path)
    return _model

def get_tokenizer():
    global _tokenizer
    if _tokenizer is None:
        tokenizer_path = os.path.join(settings.BASE_DIR, 'sentiment', 'models', 'tokenizer_2.json')
        with open(tokenizer_path) as f:
            tokenizer_data = json.load(f)
            _tokenizer = tokenizer_from_json(tokenizer_data)
    return _tokenizer
