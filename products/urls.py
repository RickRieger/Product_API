from django.urls import path
from . import views

urlpatterns = [
  path('', views.products_list),
  path('<int:pk>/', views.products_detail),
  path('reviews', views.reviews_list),
  path('reviews/<int:pk>/', views.reviews_detail),
]