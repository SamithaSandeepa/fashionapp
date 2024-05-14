from django.db import models
import uuid

class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    original_price = models.DecimalField(max_digits=6, decimal_places=2)
    discounted_price = models.DecimalField(max_digits=6, decimal_places=2)
    category_name = models.CharField(max_length=255)
    is_stock = models.BooleanField(default=True)
    rating = models.FloatField()
    reviews = models.IntegerField()
    description = models.TextField()
    trending = models.BooleanField(default=False)
    size = models.IntegerField()
    img_url = models.URLField(blank=True)

    def __str__(self):
        return self.name
