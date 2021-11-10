# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Internal:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class Category(models.Model):
    """
    This model is for a category
    """
    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(
        verbose_name=_('Name'),
        max_length=254
    )
    friendly_name = models.CharField(
        max_length=254,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    """
    This model is for a product
    """
    name = models.CharField(
        verbose_name=_('Name'),
        max_length=254
    )
    category = models.ForeignKey(
        'Category',
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )
    price = models.DecimalField(
        verbose_name=_('Price'),
        max_digits=6,
        decimal_places=2
    )
    colour = models.CharField(
        verbose_name=_('Colour'),
        max_length=254
    )
    code = models.CharField(
        verbose_name=_('Code'),
        max_length=254
    )
    description = models.TextField(
        verbose_name=_('Description'),
    )
    feature1 = models.CharField(
        verbose_name=_('Feature 1'),
        max_length=254,
        blank=True
    )
    feature2 = models.CharField(
        verbose_name=_('Feature 2'),
        max_length=254,
        blank=True
    )
    feature3 = models.CharField(
        verbose_name=_('Feature 3'),
        max_length=254,
        blank=True
    )
    feature4 = models.CharField(
        verbose_name=_('Feature 4'),
        max_length=254,
        blank=True
    )
    has_sizes = models.BooleanField(
        verbose_name=_('Has Sizes'),
        default=False,
        null=True,
        blank=True
    )
    rating = models.DecimalField(
        verbose_name=_('Rating'),
        max_digits=6,
        decimal_places=2,
        null=True,
        blank=True
    )
    pre_sale_price = models.DecimalField(
        verbose_name=_('Pre sale price'),
        max_digits=6,
        decimal_places=2,
        null=True,
        blank=True
    )
    new_release = models.BooleanField(
        default=False
    )
    image_url = models.URLField(
        verbose_name=_('Image url'),
        max_length=1024,
        null=True,
        blank=True
    )
    image = models.ImageField(
        verbose_name=_('Image'),
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name


class Review(models.Model):
    """
    This model is for a product review
    """
    RATING_CHOICES = [
        (5, '5'),
        (4, '4'),
        (3, '3'),
        (2, '2'),
        (1, '1'),
    ]
    user = models.ForeignKey(
        User,
        null=True,
        on_delete=models.SET_NULL
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )
    product_rating = models.IntegerField(
        choices=RATING_CHOICES,
        default=5
    )
    review_text = models.TextField(
        verbose_name=_('Review Text'),
        null=False,
        blank=False
    )
    create_date = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.review_text
