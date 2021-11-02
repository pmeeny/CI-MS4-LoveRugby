from django.urls import path
from . import views

urlpatterns = [
    path('', views.news_items, name='news_items'),
    path('add_news_item/', views.add_news_item, name='add_news_item'),
    path('manage_news_items/', views.manage_news_items,
         name='manage_news_items'),
    path('edit_news_item/<int:news_item_id>/', views.edit_news_item,
         name='edit_news_item'),
    path('delete_news_item/<int:news_item_id>/', views.delete_news_item,
         name='delete_news_item'),
]
