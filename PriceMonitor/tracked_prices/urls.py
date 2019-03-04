from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('pufcia/', views.pufcia, name='pufcia'),
    path('shops/', views.sklepy, name='shops'),
    path('profile/<str:username>/', views.tracked_prices_list, name='tracked_prices_list'),
    path('price/<int:pk>/', views.price_detail, name='price_detail'),
    path('price/new/', views.price_new, name='price_new'),
    path('price/<int:pk>/edit/', views.price_edit, name='price_edit'),
    path('price/<int:pk>/remove/', views.PriceDeleteView.as_view(), name='price_remove'),
]