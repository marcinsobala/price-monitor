from django.contrib import admin
from django.urls import path, include
from users import views as user_views
from django.contrib.auth import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='profile'),
    path('', include('tracked_prices.urls')),
]
