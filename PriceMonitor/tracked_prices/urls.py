from django.urls import path
from . import views

urlpatterns = [
    path('', views.tracked_prices_list, name='tracked_price_list')
]