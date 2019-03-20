import requests, re
from lxml import html

import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PriceMonitor.settings')
from django.conf import settings
django.setup()

from tracked_prices.models import TrackedPrice


def get_html_content(url):
    pageContent = requests.get(url)
    return html.fromstring(pageContent.content)


def get_name_currency(url):
    tree = get_html_content(url)
    if "allegro.pl" in url:
        name = tree.xpath('//div[@ itemtype="http://schema.org/Product"]/meta[@ itemprop="name"]/@content')
        currency = tree.xpath('//div[@ itemtype="http://schema.org/Offer"]/meta[@ itemprop="priceCurrency"]/@content')

    elif "ceneo.pl" in url:
        name = tree.xpath('//div[@ itemtype="http://schema.org/Product"]/meta[@ itemprop="name"]/@content')
        currency = tree.xpath('//div[@ itemtype="http://schema.org/Offer"]/meta[@ itemprop="priceCurrency"]/@content')

    elif "morele.net" in url:
        name = tree.xpath('//*[@ itemtype="http://schema.org/AggregateRating"]/div/span[@ itemprop="name"]/text()')
        currency = tree.xpath('//div[@ itemprop="priceCurrency"]/@content')

    elif "zalando.pl" in url:
        name = tree.xpath('//div[@ itemtype="http://schema.org/Product"]/meta[@ itemprop="name"]/@content')
        currency = tree.xpath('//div[@ itemtype="http://schema.org/Offer"]/meta[@ itemprop="priceCurrency"]/@content')


    return (name[0], currency[0])


def get_price(url):
    tree = get_html_content(url)
    if "allegro.pl" in url:
        price = tree.xpath('//div[@itemtype="http://schema.org/Offer"]/meta[@ itemprop="price"]/@content')
    elif "ceneo.pl" in url:
        price = tree.xpath('//meta[@property="og:price:amount"]/@content')
    elif "morele.net" in url:
        price = tree.xpath('//div[@itemprop="price"]/@content')
    elif "zalando.pl" in url:
        price = tree.xpath('//meta[@name="twitter:data1"]/@content')

    price = re.search(r'\d+[.,]*\d*' ,price[0]).group()
    return re.sub(r',', '.', price)


def shit():
    return TrackedPrice.objects.all()


for price in TrackedPrice.objects.values('id', 'url', 'current', 'desired', 'user_id', 'last_checked_date'):
    print(price)


unique_urls = set(TrackedPrice.objects.values_list('url'))
for i in unique_urls:
    print(get_price(i[0]))







# Algorithm first draft

# def is_obsolete(date):
#     pass
#
#
# def get_price(url):
#     price = 100
#     return (url, price)
#
#
# def update_current_price():
#     pass
#
#
# def send_mail():
#     pass
#
#
# def del_url():
#     pass
#
#
# urls = get_urls()
# urls_checked = {}
#
# for url in urls:
#
#     if is_obsolete(urls[url][4]):
#         continue
#
#     if url not in urls_checked:
#         urls_checked[url] = get_price(url)
#         update_current_price()
#
#     if urls_checked[url] <= urls[url][0]:
#         send_mail(urls[url][3])
