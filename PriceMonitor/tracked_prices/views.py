from django.shortcuts import render
from . models import TrackedPrice

def tracked_prices_list(request):
    prices = TrackedPrice.objects.all()
    return render(request, 'tracked_prices/tracked_prices_list.html', {'prices': prices})
