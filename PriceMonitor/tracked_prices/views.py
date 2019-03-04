from django.shortcuts import render, get_object_or_404, redirect
from .models import TrackedPrice, Shop
from .forms import PriceForm
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.views.generic import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from . scrape import name_price_currency
from django.contrib.auth.models import User


def home(request):
    return render(request, 'tracked_prices/home.html')


def pufcia(request):
    return render(request, 'tracked_prices/pufcia.html')


def sklepy(request):
    shops = Shop.objects.all().order_by('name')
    return render(request, 'tracked_prices/shops.html', {'shops': shops})



@login_required
def tracked_prices_list(request, username):
    user = User.objects.get(username=username)
    prices = TrackedPrice.objects.filter(user=user).order_by('-last_checked_date')
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
            return redirect('tracked_prices_list', username=request.user.username)
    else:
        form = PriceForm(instance=price)

    return render(request, 'tracked_prices/price_edit.html', {'form': form})


class PriceDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = TrackedPrice

    def test_func(self):
        price = self.get_object()
        if self.request.user == price.user:
            return True
        return False

    def get_success_url(self):
        return '/profile/' + self.request.user.username + '/'

