from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views

from users import views as user_views
from users.forms import CustomAuthenticationForm

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',
         views.LoginView.as_view(
             template_name='users/login.html',
             authentication_form=CustomAuthenticationForm),
         name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='profile'),
    path('password-reset/',
         views.PasswordResetView.as_view(
             template_name='users/password_reset.html',
             email_template_name='users/password_reset_email.html',
             subject_template_name='users/password_reset_subject.txt'
         ),
         name='password_reset'),
    path('password-reset/done',
         views.PasswordResetDoneView.as_view(
             template_name='users/password_reset_done.html'
         ),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>',
         views.PasswordResetConfirmView.as_view(
             template_name='users/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         views.PasswordResetCompleteView.as_view(
             template_name='users/password_reset_complete.html'
         ),
         name='password_reset_complete'),
    path('', include('tracked_prices.urls'))
]
