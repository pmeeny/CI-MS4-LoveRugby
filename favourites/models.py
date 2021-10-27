from django.db import models

from products.models import Product
from django.contrib.auth.models import User


class Favourites(models.Model):
    """
    This model is for a users favourites list
    """
    products = models.ManyToManyField(Product, blank=True)
    username = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.username}'s Favourites"
