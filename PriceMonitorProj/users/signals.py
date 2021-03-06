from django.contrib import messages
from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
from django.dispatch import receiver


@receiver(user_logged_in)
def on_user_logged_in(sender, request, user, **kwargs):
    messages.success(request, f"Logowanie przebiegło pomyślnie. Witaj, {user}!")


@receiver(user_logged_out)
def on_user_logged_out(sender, request, user, **kwargs):
    messages.success(request, f"Wylogowano z serwisu.")


@receiver(user_login_failed)
def on_user_login_failed(sender, request, **kwargs):
    messages.warning(request, f"Nieprawidłowy login i/lub hasło!")
