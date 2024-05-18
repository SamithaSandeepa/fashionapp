# # from django.http import JsonResponse
# # from rest_framework.views import APIView
# # from django.views.decorators.csrf import csrf_exempt
# # from django.utils.decorators import method_decorator
# # import numpy as np
# # import os
# # import json
# # from tensorflow.keras.models import load_model
# # from tensorflow.keras.preprocessing.sequence import pad_sequences
# # from tensorflow.keras.preprocessing.text import tokenizer_from_json

# # # Assuming your Django project's settings are configured to find files in the 'models' folder
# # MODEL_PATH = 'E:\\Research_new\\fashion-_frontend\\backend\\sentiment\\models\\model_name.h5'
# # TOKENIZER_PATH = 'E:\\Research_new\\fashion-_frontend\\backend\\sentiment\\models\\tokenizer.json'  # Path to your saved tokenizer

# # # Load your trained model
# # model = load_model(MODEL_PATH)

# # # Load tokenizer
# # with open(TOKENIZER_PATH, 'r', encoding='utf-8') as f:
# #     data = f.read()
# #     tokenizer = tokenizer_from_json(data)

# # @method_decorator(csrf_exempt, name='dispatch')
# # class SentimentAnalysisView(APIView):
# #     def post(self, request, *args, **kwargs):
# #         input_text = request.data.get('input_text', '')  # Correct way to access data in DRF
# #         predicted_sentiment = self.predict_sentiment(input_text)
# #         return JsonResponse({'input_text': input_text, 'predicted_sentiment': predicted_sentiment})

# #     @staticmethod
# #     def predict_sentiment(input_text):
# #         input_sequence = tokenizer.texts_to_sequences([input_text])
# #         input_sequence = pad_sequences(input_sequence, maxlen=100)
# #         predictions = model.predict(input_sequence)
# #         predicted_index = np.argmax(predictions[0])
# #         index_to_label = {0: 'negative', 1: 'slightly negative', 2: 'neutral', 3: 'slightly positive', 4: 'positive'}
# #         return index_to_label[predicted_index]






# # from django.http import JsonResponse
# # from rest_framework.views import APIView
# # from django.views.decorators.csrf import csrf_exempt
# # from django.utils.decorators import method_decorator
# # import numpy as np
# # from tensorflow.keras.models import load_model
# # from tensorflow.keras.preprocessing.sequence import pad_sequences
# # from tensorflow.keras.preprocessing.text import tokenizer_from_json
# # import os

# # # Paths to your model and tokenizer
# # MODEL_PATH = 'E:\\Research_new\\fashion-_frontend\\backend\\sentiment\\models\\model_name.h5'
# # TOKENIZER_PATH = 'E:\\Research_new\\fashion-_frontend\\backend\\sentiment\\models\\tokenizer.json'

# # # Load your trained model
# # model = load_model(MODEL_PATH)

# # # Load tokenizer
# # with open(TOKENIZER_PATH, 'r', encoding='utf-8') as f:
# #     json_string = f.read()
# #     tokenizer = tokenizer_from_json(json_string)

# # @method_decorator(csrf_exempt, name='dispatch')
# # class SentimentAnalysisView(APIView):
# #     def post(self, request, *args, **kwargs):
# #         input_text = request.data.get('input_text', '')
# #         predicted_sentiment = self.predict_sentiment(input_text)
# #         return JsonResponse({'input_text': input_text, 'predicted_sentiment': predicted_sentiment})

# #     @staticmethod
# #     def predict_sentiment(input_text):
# #         input_sequence = tokenizer.texts_to_sequences([input_text])
# #         input_sequence = pad_sequences(input_sequence, maxlen=100)
# #         predictions = model.predict(input_sequence)
# #         predicted_index = np.argmax(predictions[0])
# #         index_to_label = {0: 'negative', 1: 'slightly negative', 2: 'neutral', 3: 'slightly positive', 4: 'positive'}
# #         return index_to_label[predicted_index]




# # from django.http import JsonResponse
# # from rest_framework.views import APIView
# # from django.views.decorators.csrf import csrf_exempt
# # from django.utils.decorators import method_decorator
# # from tensorflow.keras.models import load_model
# # from tensorflow.keras.preprocessing.sequence import pad_sequences
# # from tensorflow.keras.preprocessing.text import tokenizer_from_json
# # import numpy as np
# # import os
# # import json

# # # Assuming your Django project's settings are configured to find files in the 'models' folder
# # MODEL_PATH = 'E:\\Research_new\\fashion-_frontend\\backend\\sentiment\\models\\model_name_2.h5'
# # TOKENIZER_PATH = 'E:\\Research_new\\fashion-_frontend\\backend\\sentiment\\models\\tokenizer_2.json'

# # # Initialize model and tokenizer as None to load them lazily
# # model = None
# # tokenizer = None

# # def load_sentiment_model():
# #     """Lazily load the sentiment analysis model."""
# #     global model
# #     if model is None:
# #         model = load_model(MODEL_PATH)
# #     return model

# # def load_tokenizer():
# #     """Lazily load the tokenizer."""
# #     global tokenizer
# #     if tokenizer is None:
# #         with open(TOKENIZER_PATH, 'r', encoding='utf-8') as f:
# #             json_string = f.read()
# #             tokenizer = tokenizer_from_json(json_string)
# #     return tokenizer

# # @method_decorator(csrf_exempt, name='dispatch')
# # class SentimentAnalysisView(APIView):
# #     def post(self, request, *args, **kwargs):
# #         input_text = request.data.get('input_text', '')
# #         # Ensure the model and tokenizer are loaded
# #         model = load_sentiment_model()
# #         tokenizer = load_tokenizer()
# #         predicted_sentiment = self.predict_sentiment(input_text, tokenizer, model)
# #         return JsonResponse({'input_text': input_text, 'predicted_sentiment': predicted_sentiment})

# #     @staticmethod
# #     def predict_sentiment(input_text, tokenizer, model):
# #         """Predict sentiment from input text using the loaded model and tokenizer."""
# #         input_sequence = tokenizer.texts_to_sequences([input_text])
# #         input_sequence = pad_sequences(input_sequence, maxlen=100)
# #         predictions = model.predict(input_sequence)
# #         predicted_index = np.argmax(predictions[0])
# #         index_to_label = {0: 'negative', 1: 'slightly negative', 2: 'neutral', 3: 'slightly positive', 4: 'positive'}
# #         return index_to_label[predicted_index]



# # views.py for the sentiment analysis Django app

# from django.http import JsonResponse
# from django.views import View
# from django.views.decorators.csrf import csrf_exempt
# from django.utils.decorators import method_decorator
# from tensorflow.keras.preprocessing.sequence import pad_sequences
# import numpy as np
# from .sentiment_resources import get_model, get_tokenizer
# # Import the global variables from your apps.py
# from .apps import SentimentConfig

# # def predict_sentiment(input_text, tokenizer, model):
# #     # Convert the input text to a sequence of integers
# #     input_sequence = tokenizer.texts_to_sequences([input_text])

# #     # Pad the sequence so it's of the correct length
# #     input_sequence = pad_sequences(input_sequence, maxlen=100)

# #     # Predict the sentiment of the input text
# #     predictions = model.predict(input_sequence)

# #     # Find the index of the highest prediction
# #     predicted_index = np.argmax(predictions[0])

# #     # Map the index to the corresponding sentiment label
# #     index_to_label = {0: 'negative', 1: 'slightly negative', 2: 'neutral', 3: 'slightly positive', 4: 'positive'}

# #     # Return the predicted sentiment label
# #     return index_to_label[predicted_index]

# def predict_sentiment(input_text):
#     tokenizer = get_tokenizer()
#     model = get_model()

# @method_decorator(csrf_exempt, name='dispatch') # Consider the security implications in production
# # class SentimentAnalysisView(View):
# #     def post(self, request, *args, **kwargs):
# #         # Extract the comment from the POST request
# #         input_text = request.POST.get("comment", "")
        
# #         # Use the globally loaded tokenizer and model
# #         predicted_sentiment = predict_sentiment(input_text, SentimentConfig.tokenizer, SentimentConfig.model)
        
# #         # Return the predicted sentiment as a JSON response
# #         return JsonResponse({"input": input_text, "predicted_sentiment": predicted_sentiment})
    
# class SentimentAnalysisView(View):
#     def post(self, request, *args, **kwargs):
#         input_text = request.POST.get("comment", "")
        
#         predicted_sentiment = predict_sentiment(input_text)
        
#         return JsonResponse({"input": input_text, "predicted_sentiment": predicted_sentiment})

import os
import json
from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from tensorflow.keras.preprocessing.sequence import pad_sequences
import numpy as np
from concurrent.futures import ThreadPoolExecutor, as_completed
from lime.lime_text import LimeTextExplainer
import htmlmin
from django.conf import settings

from .sentiment_resources import get_model, get_tokenizer

def predict_sentiment(input_text,explainable_ai=False):
    tokenizer = get_tokenizer()
    model = get_model()
    input_sequence = tokenizer.texts_to_sequences([input_text])
    input_sequence = pad_sequences(input_sequence, maxlen=100)

    predictions = model.predict(input_sequence)
    predicted_index = np.argmax(predictions[0])
    index_to_label = {0: 'negative', 1: 'slightly-negative', 2: 'neutral', 3: 'slightly-positive', 4: 'positive'}

    # class_names = ['negative', 'slightly negative', 'neutral', 'slightly positive', 'positive']     
    explainer = LimeTextExplainer(class_names=index_to_label)
    def predict_proba(texts):
        seqs = tokenizer.texts_to_sequences(texts)
        padded_seqs = pad_sequences(seqs, maxlen=100)
        return model.predict(padded_seqs)

    # def generate_explanation(text):
    #     exp = explainer.explain_instance(text, predict_proba, num_features=10)
    #     # For non-notebook environments, you might return exp.as_list() or another format
    #     return exp

    # E xplain a specific prediction
    #idx = 107  # Example index
    explanations = ''
    if explainable_ai:
        exp = explainer.explain_instance(input_text , predict_proba, num_features=10)
        # explanations= htmlmin.minify(exp.as_html())
        annotated_file_name = "explanations.html"
        save_dir = os.path.join(settings.MEDIA_ROOT, annotated_file_name)
        # annotated_image_path = os.path.join(save_dir, annotated_file_name)
        exp.save_to_file(save_dir)
        explanations = annotated_file_name

    # exp.as_html()
    # Use ThreadPoolExecutor to parallelize explanation generation
    # with ThreadPoolExecutor(max_workers=5) as executor:
    #     # Submit all the tasks and get future objects
    #     futures = [executor.submit(generate_explanation, text) for text in input_text]

    #     # Wait for the futures to complete and get results
    #     for future in as_completed(futures):
    #         exp = future.result()
    #         # If using in a Jupyter Notebook
    #         expList.append(exp.as_html())

    return {
        "index_to_label": index_to_label[predicted_index],
        "explanations": explanations

    }

@method_decorator(csrf_exempt, name='dispatch')
class SentimentAnalysisView(View):
    # def post(self, request, *args, **kwargs):
        # input_text = request.POST.get("comment", "")
        # print(input_text)
        # predicted_sentiment = predict_sentiment(input_text)
        # return JsonResponse({"input": input_text, "predicted_sentiment": predicted_sentiment})
        def post(self, request, *args, **kwargs):
        # Load the JSON data from the request body
            data = json.loads(request.body.decode('utf-8'))
            # input_text = request.POST.get("comment", "")
            # print( decode(request.POST.get("comment")))
            # Extract the list of comments from the JSON data
            comments = data['comment']
            explainable_ai = data['explainable_ai'] if 'explainable_ai' in data else False
            print(comments)
            # comments = data.get("comments", [])
            # Initialize an empty list to store the results
            
            results = []
            # Iterate over each comment in the received list of comments
            for comment in comments:
                predicted_sentiment = predict_sentiment(comment,explainable_ai)
                results.append({
                    "comment": comment,
                    "predicted_sentiment": predicted_sentiment["index_to_label"],
                    "explanations": predicted_sentiment["explanations"]
                })
                
            
            # Return the list of comments with their predicted sentiments
            return JsonResponse({"results": results})
        
                

