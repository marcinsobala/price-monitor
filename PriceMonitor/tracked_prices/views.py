from django.shortcuts import render, get_object_or_404, redirect
from .models import TrackedPrice
from .forms import PriceForm
from django.utils import timezone

def tracked_prices_list(request):
    prices = TrackedPrice.objects.all().order_by('-last_checked_date')
    return render(request, 'tracked_prices/tracked_prices_list.html', {'prices': prices})


def price_detail(request, pk):
    price = get_object_or_404(TrackedPrice, pk=pk)
    return render(request, 'tracked_prices/price_detail.html', {'price': price})


def price_new(request):
    if request.method == "POST":
        form = PriceForm(request.POST)
        if form.is_valid():
            price = form.save(commit=False)
            price.name = "Some name"
            price.current = 0
            price.currency = "PLN"
            price.user = request.user
            price.last_checked_date = timezone.now()
            price.save()
            return redirect('price_detail', pk=price.pk)
    else:
        form = PriceForm()

    return render(request, 'tracked_prices/price_new.html', {'form': form})

