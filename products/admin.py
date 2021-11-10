# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.contrib import admin

# Internal:
from .models import Product, Category, Review
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class ProductAdmin(admin.ModelAdmin):
    """
    Admin class for the Product model.
    """
    list_display = (
        'code',
        'name',
        'category',
        'has_sizes',
        'price',
        'pre_sale_price',
        'rating',
        'image',
        'image_url',
    )

    ordering = ('code',)


class CategoryAdmin(admin.ModelAdmin):
    """
    Admin class for the Category model.
    """
    list_display = (
        'friendly_name',
        'name',
    )


class ReviewAdmin(admin.ModelAdmin):
    """
    Admin class for the Review model.
    """
    list_display = (
        'user',
        'product',
        'product_rating',
        'review_text',
        'create_date',
    )
    list_filter = (
        'user',
        'product',
        'product_rating',
        'create_date',
    )
    search_fields = (
        'user',
        'product',
        'product_rating'
        'review_text',
    )
    list_per_page = 20


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Review, ReviewAdmin)
