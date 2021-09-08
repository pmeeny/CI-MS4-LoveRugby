from django.contrib import admin
from .models import Product, Category, Sizes

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'code',
        'name',
        'category',
        'price',
        'rating',
        'image',
    )

    ordering = ('code',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Sizes)