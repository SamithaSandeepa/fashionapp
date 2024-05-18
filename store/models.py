from django.db import models
import uuid

class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    gender = models.CharField(max_length=6)
    image_search_label = models.CharField(max_length=255)
    original_price = models.DecimalField(max_digits=10, decimal_places=2)
    discounted_price = models.DecimalField(max_digits=10, decimal_places=2)
    fashion_style = models.CharField(max_length=255)
    fashion_brand = models.CharField(max_length=255)
    cloth_type = models.CharField(max_length=255)
    garment_fitting = models.CharField(max_length=255)
    description = models.TextField()
    img_url = models.URLField(blank=True)

    def __str__(self):
        return self.name
