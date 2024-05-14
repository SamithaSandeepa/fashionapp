import uuid
from django.db import models

class Comments(models.Model):
    product_id = models.UUIDField(default=uuid.uuid4, editable=True)
    comments=models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    
