from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('search_reviews/', views.search_reviews, name='search_reviews'),
    path('filter_reviews/', views.filter_reviews, name='filter_reviews'),
    path('sort_reviews/', views.sort_reviews, name='sort_reviews'),
]
