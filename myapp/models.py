# myapp/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

# Define the CustomUser model
class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        (1, 'customer'),
        (2, 'seller'),
    )
    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES)
    # You can add other fields specific to the user here

class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    gender = models.CharField(max_length=10, blank=True, null=True)
    ageGroup = models.CharField(max_length=10, blank=True, null=True)
    province = models.CharField(max_length=50, blank=True, null=True)
    hobby = models.CharField(max_length=50, blank=True, null=True)
    color = models.CharField(max_length=50, blank=True, null=True)
    sport = models.CharField(max_length=50, blank=True, null=True)
    Openness_Level = models.CharField(max_length=10, blank=True, null=True)
    Conscientiousness_Level = models.CharField(max_length=10, blank=True, null=True)
    Extroversion_Level = models.CharField(max_length=10, blank=True, null=True)
    Agreeableness_Level = models.CharField(max_length=10, blank=True, null=True)
    Neuroticism_Level = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return f'{self.user.username} Profile'