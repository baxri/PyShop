from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=254)
    price = models.FloatField(default=0)
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2083)
