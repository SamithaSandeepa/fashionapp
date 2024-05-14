from django.urls import path
from .views import SentimentAnalysisView

urlpatterns = [
    path('sentiment_analysis', SentimentAnalysisView.as_view(), name='sentiment_analysis'),
    
]
