from django.urls import path
from .views import PredictPersonalityView, PredictFashionView

urlpatterns = [
    path('predict-personality/', PredictPersonalityView.as_view(), name='predict-personality'),
    path('predict-fashion/', PredictFashionView.as_view(), name='predict-fashion'),

]
