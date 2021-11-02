from django.urls import path
from . import views

urlpatterns = [
    path('view_product_favourites/', views.view_product_favourites,
         name='view_product_favourites'),
    path('add_product_to_favourites/<item_id>/',
         views.add_product_to_favourites, name='add_product_to_favourites'),
    path('remove_product_from_favourites/<item_id>/<redirect_from>/',
         views.remove_product_from_favourites,
         name='remove_product_from_favourites'),
]
