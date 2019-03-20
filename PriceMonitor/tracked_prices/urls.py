from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('pufcia/', views.pufcia, name='pufcia'),
    path('shops/', views.sklepy, name='shops'),
    path('prices/', views.tracked_prices_list, name='tracked_prices_list'),
    path('price/new/', views.price_new, name='price_new'),
    path('price/<int:pk>/edit/', views.price_edit, name='price_edit'),
    path('price/<int:pk>/remove/', views.PriceDeleteView.as_view(), name='price_remove'),
]