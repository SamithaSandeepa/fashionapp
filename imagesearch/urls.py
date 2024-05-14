from django.urls import path
from .views import ObjectDetection

urlpatterns = [
    path('detect', ObjectDetection.as_view(), name='object_detection'),
    # path('test', Test.as_view(), name='test'),

]
