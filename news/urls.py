from django.urls import path
from . import views

urlpatterns = [
    path('', views.news_items, name='news_items'),
    path('add_news_item/', views.add_news_item, name='add_news_item'),
    path('manage_news_items/', views.manage_news_items, name='manage_news_items'),
]
