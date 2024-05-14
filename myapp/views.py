# myapp/views.py
from django.contrib.auth import get_user_model, authenticate
from rest_framework import generics, views, permissions, status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from .serializers import CustomUserSerializer, UserProfileSerializer
from .models import UserProfile
from rest_framework.permissions import IsAuthenticated

class CustomUserCreate(generics.CreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = CustomUserSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        user = get_user_model().objects.get(id=response.data['id'])
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key, 'user_id': response.data['id']})

class LoginView(views.APIView):

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)

        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({"token": token.key})
        else:
            return Response({"error": "Wrong Credentials"}, status=status.HTTP_400_BAD_REQUEST)
        
class LogoutView(views.APIView):
    def post(self, request):
        request.auth.delete()
        return Response(status=status.HTTP_200_OK)
    
from rest_framework import generics, permissions
from .models import UserProfile
from .serializers import UserProfileSerializer

class UserProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return UserProfile.objects.filter(user=self.request.user)

    def get_object(self):
        obj, created = UserProfile.objects.get_or_create(user=self.request.user)
        return obj