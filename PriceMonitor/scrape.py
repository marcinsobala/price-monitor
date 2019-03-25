import requests, re
from lxml import html

#Following 4 lines enable scrape.py to use Django ORM
import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PriceMonitor.settings')
from django.conf import settings
django.setup()

from django.utils import timezone
from django.db import Q
from tracked_prices.models import TrackedPrice
from users.models import User


def get_html_content(url):
    pageContent = requests.get(url)
    return html.fromstring(pageContent.content)

# TODO - is currency necessary? May need to regex jsons to get it
def get_name_price_currency(url):
    tree = get_html_content(url)
    if "allegro.pl" in url:
        name = tree.xpath('//meta[@property="og:title"]/@content')
        price = tree.xpath('//meta[@itemprop="price"]/@content')
        currency = tree.xpath('//meta[@itemprop="priceCurrency"]/@content')

    elif "ceneo.pl" in url:
        name = tree.xpath('//meta[@property="og:title"]/@content')
        price = tree.xpath('//meta[@property="og:price:amount"]/@content')
        currency = tree.xpath('//meta[@property="og:price:currency"]/@content')

    elif "morele.net" in url:
        name = tree.xpath('//*[@itemtype="http://schema.org/AggregateRating"]/div/span[@itemprop="name"]/text()')
        price = tree.xpath('//div[@itemprop="price"]/@content')
        currency = tree.xpath('//div[@ itemprop="priceCurrency"]/@content')

    elif "zalando.pl" in url:
        name = tree.xpath('//meta[@property="og:title"]/@content')
        price = tree.xpath('//meta[@name="twitter:data1"]/@content')
        currency = ["PLN"]

    if type(price) == list:
        price = price[0]

    price = re.search(r'\d+[.,]*\d*' ,price).group()
    price = re.sub(r',', '.', price)

    return name[0], price, currency[0]


# scrapes html for a price location, then regexes it to specific format
def get_price(url):
    tree = get_html_content(url)
    if "allegro.pl" in url:
        price = tree.xpath('//meta[@itemprop="price"]/@content')
    elif "ceneo.pl" in url:
        price = tree.xpath('//meta[@property="og:price:amount"]/@content')
    elif "morele.net" in url:
        price = tree.xpath('//div[@itemprop="price"]/@content')
    elif "zalando.pl" in url:
        price = tree.xpath('//meta[@name="twitter:data1"]/@content')

    if type(price) == list:
        price = price[0]

    price = re.search(r'\d+[.,]*\d*' ,price).group()
    return re.sub(r',', '.', price)


def shit():
    return TrackedPrice.objects.all()

# Returns query set of all necessary tracked price data
def tracked_price_data():
    return TrackedPrice.objects.values('url', 'current', 'desired',
                                       'percent_drop', 'user_id', 'when_inform')


# Returns a generator of urls and their new prices dictionary
def scrape_current_prices():
    unique_urls = set(TrackedPrice.objects.values_list('url'))
    for url in unique_urls:
        yield {'url': url[0], 'current': get_price(url[0])}


# If difference is found between scraped and current price in db, price is updated
def update_current_prices():
    for scraped_price in scrape_current_prices():
        TrackedPrice.objects.filter(url=scraped_price['url'], ~Q(current=scraped_price['current'])).update(
            current=scraped_price['current'],
            last_checked_date=timezone.now())


def prepare_emails():
    pass


def main():
    prices = tracked_price_data()
    update_current_prices()
    updated_prices = tracked_price_data()



# unique_urls = set(TrackedPrice.objects.values_list('url'))
# for i in ({'url': k[0], 'current': get_price(k[0])} for k in unique_urls):
#     print(i)
