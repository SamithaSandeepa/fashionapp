from django.views import View
from django.http import JsonResponse
import pandas as pd
import pickle
import os
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser

# Mapping of predicted values to target trait levels
trait_levels = {
    0: 'Low',
    1: 'High'
}

class PredictPersonalityView(APIView):
    parser_classes = [JSONParser]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        model_file = os.path.join(os.path.dirname(__file__), 'models', 'personality_model.pkl') 
        with open(model_file, 'rb') as file:
            self.model = pickle.load(file)

    def post(self, request, *args, **kwargs):
        # Directly use the request data if it's already a list
        encoded_array = request.data if isinstance(request.data, list) else request.data.get("data", [])
        print(encoded_array)

        # Ensure the encoded_array is not empty
        if not encoded_array:
            return JsonResponse({'error': 'No data provided'}, status=400)

        # Convert the encoded array into a DataFrame
        df_sample = pd.DataFrame([encoded_array])

        try:
            # Make the prediction
            predictions = self.model.predict(df_sample)
            predictions_list = predictions.tolist()  # Convert predictions to a list for JSON serialization
            # Map predicted values to target trait levels
            mapped_predictions = [trait_levels[pred] for pred in predictions_list[0]]

            return JsonResponse({'predictions': mapped_predictions})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
        

# [
#     1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0
# ]
# sample = [
#     1,  # Gender_Female
#     0,  # Gender_Male
#     0,  # Age Category_0-19
#     0,  # Age Category_20-29
#     1,  # Age Category_30-39
#     0,  # Age Category_40-49
#     0,  # Age Category_50-59
#     0,  # Age Category_60+
#     0,  # Location _Central
#     0,  # Location _Eastern
#     0,  # Location _North Central
#     0,  # Location _North Western
#     1,  # Location _Northern
#     0,  # Location _Sabaragamuwa
#     0,  # Location _Southern
#     0,  # Location _Uva
#     0,  # Location _Western
#     0,  # Hobby_Cooking
#     0,  # Hobby_Cricket
#     0,  # Hobby_Other
#     0,  # Hobby_Painting
#     1,  # Hobby_Reading
#     0,  # Hobby_Sports
#     0,  # Hobby_Travelling
#     0,  # Hobby_Watching Movies
#     0,  # Favorite Color_Black
#     1,  # Favorite Color_Blue
#     0,  # Favorite Color_Green
#     0,  # Favorite Color_Other
#     0,  # Favorite Color_Purple
#     0,  # Favorite Color_Red
#     0,  # Favorite Color_White
#     0,  # Favorite Color_Yellow
#     0,  # Sport_BallSports
#     1,  # Sport_Cricket
#     0,  # Sport_No Sport
#     0,  # Sport_Other
#     0,  # Sport_Running
#     0,  # Sport_Soccer
#     0,  # Sport_Swimming
#     0   # Sport_Tennis
# ]

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import pandas as pd
import pickle
import numpy as np
import os

# Load your model
model_path = os.path.join(os.path.dirname(__file__), 'models', 'anji_model2.pkl')
with open(model_path, 'rb') as file:
    model = pickle.load(file)

class PredictFashionView(APIView):
    def post(self, request, *args, **kwargs):
        # Initialize sample data with all 0
        sample_data = {
            'Gender_Female': [0],
            'Gender_Male': [0],
            'Favorite Color_Blue': [0],
            'Favorite Color_Green': [0],
            'Favorite Color_Other': [0],
            'Favorite Color_Purple': [0],
            'Favorite Color_Red': [0],
            'Favorite Color_White': [0],
            'Favorite Color_Yellow': [0],
            'Openness Level_High': [0],
            'Openness Level_Low': [0],
            'Conscientiousness Level_High': [0],
            'Conscientiousness Level_Low': [0],
            'Extroversion Level_High': [0],
            'Extroversion Level_Low': [0],
            'Agreeableness Level_High': [0],
            'Agreeableness Level_Low': [0],
            'Neuroticism Level_High': [0],
            'Neuroticism Level_Low': [0],
            'Age Category_0-19': [0],
            'Age Category_20-29': [0],
            'Age Category_30-39': [0],
            'Age Category_40-49': [0],
            'Age Category_50-59': [0],
            'Age Category_60+': [0],
        }
# sample_data = {
#             'Gender_Female': [0],
#             'Gender_Male': [0],
#             'Favorite Color_Blue': [0],
#             'Favorite Color_Green': [0],
#             'Favorite Color_Other': [0],
#             'Favorite Color_Purple': [0],
#             'Favorite Color_Red': [0],
#             'Favorite Color_White': [0],
#             'Favorite Color_Yellow': [0],
#             'Openness Level_High': [0],
#             'Openness Level_Low': [0],
#             'Conscientiousness Level_High': [0],
#             'Conscientiousness Level_Low': [0],
#             'Extroversion Level_High': [0],
#             'Extroversion Level_Low': [0],
#             'Neuroticism'+request.data['Neuroticism']: 1,
#             'Age': 1,
#         }
        # Update sample_data based on request data
        user_data = request.data
        for key in user_data:
            if key in sample_data:
                sample_data[key] = [user_data[key]]

        # Convert the dictionary to a DataFrame
        sample_df = pd.DataFrame(sample_data)

        # Predict
        predicted_values = model.predict(sample_df)

        # Decode the prediction (Assuming a binary classification for each label)
        def decode_prediction(predicted_output, target_columns):
            predicted_classes = [target_columns[idx] for idx, value in enumerate(predicted_output[0]) if value == 1]
            return predicted_classes

        # Sample target variable columns (adjust according to your model's output)
        target_columns = [
            'fashion_style Casual', 'fashion_style Formal', 'fashion_style Minimalist', 'fashion_style Other', 'fashion_style Sporty', 'fashion_style Vintage',
            'fashion_brand Adidas', 'fashion_brand Gucci', 'fashion_brand H&M', 
            'fashion_brand Nike', 
            'fashion_brand No_Brand', 'fashion_brand Other', 'fashion_brand Zara',
            'cloth_type Bottoms', 'cloth_type Dresses', 'cloth_type Footwear', 'cloth_type Type_Other', 'cloth_type Shirt', 'cloth_type Skirt', 'cloth_type T-shirt', 'cloth_type Tops', 'cloth_type Trouser',
            'garment_fitting Baggy', 'garment_fitting Classic Fit', 'garment_fitting Other', 'garment_fitting Regular Fit', 'garment_fitting Slim_Fit'
        ]


        # Decode the prediction
        predicted_classes = decode_prediction(predicted_values, target_columns)
        print("Predicted Classes:", predicted_classes)

        return Response(predicted_classes, status=status.HTTP_200_OK)
