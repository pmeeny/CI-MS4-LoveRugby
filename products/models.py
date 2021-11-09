# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Internal:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(
        verbose_name=_("Name"),
        max_length=254
    )
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    name = models.CharField(max_length=254)
    category = models.ForeignKey(
        'Category',
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )
    price = models.DecimalField(max_digits=6, decimal_places=2)
    colour = models.CharField(max_length=254)
    code = models.CharField(max_length=254)
    description = models.TextField()
    feature1 = models.CharField(max_length=254, blank=True)
    feature2 = models.CharField(max_length=254, blank=True)
    feature3 = models.CharField(max_length=254, blank=True)
    feature4 = models.CharField(max_length=254, blank=True)
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True,
                                 blank=True)
    pre_sale_price = models.DecimalField(max_digits=6, decimal_places=2,
                                         null=True, blank=True)
    new_release = models.BooleanField(default=False)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class Review(models.Model):
    RATING_CHOICES = [
        (5, '5'),
        (4, '4'),
        (3, '3'),
        (2, '2'),
        (1, '1'),
    ]
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_rating = models.IntegerField(choices=RATING_CHOICES,
                                         default=5)
    review_text = models.TextField(null=False, blank=False)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.review_text
