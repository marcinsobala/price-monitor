from django.urls import path
from . import views

urlpatterns = [
    path('', views.tracked_prices_list, name='tracked_price_list'),
    path('price/<int:pk>/', views.price_detail, name='price_detail'),
    path('price/new/', views.price_new, name='price_new'),
]