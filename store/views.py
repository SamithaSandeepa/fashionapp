from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer
from django.shortcuts import render
from firebase_admin import storage
import firebase_admin
from firebase_admin import credentials
from myproject import settings
import os
from .utils import upload_image_to_firebase


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        instance = serializer.save()

        # Check if image is included in request
        if 'img_url' in self.request.FILES:
            file = self.request.FILES['img_url']
            file_name = f'{instance.id}_{file.name}'  # Create a unique file name
            print(file_name)
            # Upload image to Firebase Storage
            img_url = upload_image_to_firebase(file, file_name)
            print(img_url)
            if img_url:
                # Save the Firebase Storage URL to the instance
                instance.img_url = img_url
                instance.save()

    def perform_update(self, serializer):
        instance = serializer.save()

        # Check if image is included in request
        if 'img_url' in self.request.FILES:
            file = self.request.FILES['img_url']
            file_name = f'{instance.id}_{file.name}'  # Create a unique file name
            print(file_name)
            # Upload image to Firebase Storage
            img_url = upload_image_to_firebase(file, file_name)
            print(img_url)
            if img_url:
                # Save the Firebase Storage URL to the instance
                instance.img_url = img_url
                instance.save()