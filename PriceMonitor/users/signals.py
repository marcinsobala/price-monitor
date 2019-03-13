from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.dispatch import receiver
from django.contrib import messages
from django.shortcuts import render, redirect



@receiver(user_logged_in)
def on_user_logged_in(sender, request, user, **kwargs):
    messages.success(request, f"Logowanie przebiegło pomyślnie. Witaj, {user}!")

@receiver(user_logged_out)
def on_user_logged_out(sender, request, user, **kwargs):
    messages.success(request, f"Wylogowano z serwisu.")


