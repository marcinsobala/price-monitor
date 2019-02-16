from django.shortcuts import render, get_object_or_404, redirect
from .models import TrackedPrice
from .forms import PriceForm
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from . scrape import name_price_currency


def tracked_prices_list(request):
    prices = TrackedPrice.objects.all().order_by('-last_checked_date')
    return render(request, 'tracked_prices/tracked_prices_list.html', {'prices': prices})


def price_detail(request, pk):
    price = get_object_or_404(TrackedPrice, pk=pk)
    return render(request, 'tracked_prices/price_detail.html', {'price': price})


@login_required
def price_new(request):
    if request.method == "POST":
        form = PriceForm(request.POST)
        if form.is_valid():
            price = form.save(commit=False)
            price.name, price.current, price.currency = name_price_currency(price.url)
            price.user = request.user
            price.last_checked_date = timezone.now()
            price.save()
            return redirect('price_detail', pk=price.pk)
    else:
        form = PriceForm()

    return render(request, 'tracked_prices/price_new.html', {'form': form})


@login_required
def price_edit(request, pk):
    price = get_object_or_404(TrackedPrice, pk=pk)
    if request.method == "POST":
        form = PriceForm(request.POST, instance=price)
        if form.is_valid():
            price = form.save(commit=False)
            price.name, price.current, price.currency = name_price_currency(price.url)
            price.last_checked_date = timezone.now()
            price.save()
            return redirect('price_detail', pk=price.pk)
    else:
        form = PriceForm(instance=price)

    return render(request, 'tracked_prices/price_edit.html', {'form': form})


@login_required
def price_remove(request, pk):
    price = get_object_or_404(TrackedPrice, pk=pk)
    price.delete()
    return redirect('tracked_prices_list')