from django.db import models

# Create your models here.

class Product(models.Model):
    prouct_name = models.CharField(max_length=200)
    product_price = models.IntegerField()
    product_weight = models.FloatField()
    created_at = models.CharField(max_length=200)
    updated_at = models.CharField(max_length=200)