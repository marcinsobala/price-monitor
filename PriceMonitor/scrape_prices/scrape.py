""" Module is used to get price and product data from urls provided by the
    users, automatically update those prices in db and notify users via e-mail
    when price drop met their expectations
"""

import os
import sys
import re
import requests
import time
import asyncio
import aiohttp
from lxml import html
from operator import itemgetter

import django
from django.utils import timezone
from django.core.mail import send_mail

# TODO remove before deployment. No need to set up environemnt when site is up
# Following 3 lines enable module to use Django ORM  and app imports when run outside of website
sys.path.append('..')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PriceMonitor.PriceMonitor.settings')
django.setup()

from django.conf import settings
from django.contrib.auth.models import User
from tracked_prices.models import TrackedPrice, Shop
from scrape_prices import shop_xpaths


async def get_html_content_async(url, session):
    # Returns html content of url. Async ready.
    try:
        async with session.get(url) as pageContent:
            return html.fromstring(await pageContent.text())
    except Exception as e:
        return None


def get_html_content(url):
    # Returns html content of url.
    try:
        return html.fromstring(requests.get(url).text)
    except requests.exceptions.RequestException:
        raise ConnectionError


def get_name_price_currency(url):
    # Returns name, price and currency from url, based on xpaths stored in dict initialized in init.py
    tree = get_html_content(url)
    shop = re.search(r'https?://(www\.)?(.*?)/', url).group(2)

    name = tree.xpath(shop_xpaths[shop]['name'])[0].strip()
    price = tree.xpath(shop_xpaths[shop]['price'])[0].strip()
    currency = tree.xpath(shop_xpaths[shop]['currency'])[0].strip()

    # Exceptions for websites which just can't store their metadata normally
    if shop == 'zalando.pl':
        currency = currency.split()[-1]
    elif shop in ['agdmaster.com', 'diabetyk24.pl', 'krakvet.pl', 'olx.pl', 'zooart.com.pl']:
        currency = 'PLN'

    if currency.strip().upper() == 'ZŁ': currency = 'PLN'

    price = re.search(r'\d+ *[.,]*\d*', price).group()
    price = re.sub(r',', '.', price)
    price = re.sub(r' ', '', price)

    return name, price, currency


async def get_price(url, session, scraped_prices):
    """ Appends a tuple of price from url and url to list provided
        in arguments, based on xpaths stored in dict initialized in init.py. Async ready
    """
    tree = await get_html_content_async(url, session)
    shop = re.search(r'https?://(www\.)?(.*?)/', url).group(2)

    try:
        price = tree.xpath(shop_xpaths[shop]['price'])[0]
    except Exception as e:
        TrackedPrice.objects.filter(url=url).update(name='# Produkt zniknął ze strony :/ Najlepiej go usunąć')
        return None

    price = re.search(r'\d+ *[.,]*\d*', price).group()
    price = re.sub(r',', '.', price)
    price = re.sub(r' ', '', price)

    scraped_prices.append((url, price))


def tracked_price_data():
    # Returns query set of all necessary tracked price data
    return TrackedPrice.objects.values('id', 'user_id', 'when_inform', 'current',
                                       'desired', 'percent_drop', 'url')


async def update_current_prices():
    """ Asynchronously searches for current prices in unique urls from database,
        then updates prices current value and last checked date
    """
    unique_urls = TrackedPrice.objects.values_list('url').distinct().order_by('url')
    async with aiohttp.ClientSession() as session:
        tasks = []
        scraped_prices = []
        for url in unique_urls:
            task = asyncio.create_task(get_price(url[0], session, scraped_prices))
            tasks.append(task)
        await asyncio.gather(*tasks)

    for price in scraped_prices:
        TrackedPrice.objects.filter(url=price[0]).update(current=price[1], last_checked_date=timezone.now())


def is_price_satisfactory(old_prices):
    """ Checks if prices dropped according to users wishes and returns a list of tuples
        with prices id's and users id's sorted by users id's
    """
    id_list = []
    new_prices = TrackedPrice.objects.values("current")

    for i in range(len(old_prices)):
        if new_prices[i]['current'] < old_prices[i]['current']:

            # Price has to drop
            if old_prices[i]["when_inform"] == "A":
                id_list.append((old_prices[i]['id'], old_prices[i]['user_id']))

            # Price has to drop by a percent
            elif old_prices[i]["when_inform"] == "B":
                if new_prices[i]['current'] <= old_prices[i]['desired'] * (1 - old_prices[i]['percent_drop'] / 100):
                    id_list.append((old_prices[i]['id'], old_prices[i]['user_id']))

            # Price has to drop to a desired value
            elif old_prices[i]['when_inform'] == "C":
                if new_prices[i]['current'] <= old_prices[i]['desired']:
                    id_list.append((old_prices[i]['id'], old_prices[i]['user_id']))

    id_list.sort(key=itemgetter(1))
    return id_list


def prepare_emails(prices_users_IDs):
    # Returns list of dictionaries with email addresses and prepared messages
    email_index = -1
    prepared_emails = []
    previous_user_id = ""

    for id, user_id in prices_users_IDs:
        price = TrackedPrice.objects.get(id=id)
        message = f"Cena {price.name} spadła do {price.current} {price.currency}!\n{price.url}\n\n"

        # Appends to previous message if it's the price belonging to the same user,
        # otherwise creates a new message
        if user_id != previous_user_id:
            user = User.objects.get(id=user_id)
            message = f"{user.username},\n\n{message}"
            prepared_emails.append({'email': user.email,
                                    'subject': "Śledzone ceny spadły!",
                                    'message': message})
            email_index += 1
            previous_user_id = user_id
        else:
            prepared_emails[email_index]['message'] += message

    for email in prepared_emails:
        email['message'] += 'Udanych zakupów, \nZespół Cebula Hunter'

    return prepared_emails


# TODO Secure password and mail with Heroku environ
def send_mails(prepared_emails):
    for message in prepared_emails:
        send_mail(message['subject'],
                  message['message'],
                  settings.EMAIL_HOST_USER,
                  recipient_list=(message['email'],),
                  auth_password=settings.EMAIL_HOST_PASSWORD)


def price_drop_inform():
    # Updates prices and sends out emails if prices are now satisfactory for the user
    old_prices = list(tracked_price_data())
    asyncio.run(update_current_prices())
    prices_users_IDs = is_price_satisfactory(old_prices)

    # No point in running these functions if no prices are satisfactory
    if prices_users_IDs:
        prepared_emails = prepare_emails(prices_users_IDs)
        send_mails(prepared_emails)


def add_shops_from_dict_to_db():
    shops_added = []
    for shop in Shop.objects.all():
        shops_added.append(shop.name)

    shops_to_add = []
    for shop in shop_xpaths.keys():
        if shop not in shops_added:
            shops_to_add.append(shop)

    for shop in shops_to_add:
        new_shop = Shop(name=shop, url=f"https://{shop}/")
        new_shop.save()

    print(shops_to_add)


if __name__ == "__main__":
    # Left here for testing purposes only

    # start_time = time.time()
    # asyncio.run(update_current_prices())
    # duration = time.time() - start_time
    # print(duration)
    # print(get_name_price_currency('https://www.123lazienka.pl/pl/p/DEANTE-MODERN-ZLEWOZMYWAK-1%2C5-KOMOROWY-Z-OCIEKACZEM-ALABASTER-GRANIT-100-x-52-cm-ZQM-A513/20553'))
    add_shops_from_dict_to_db()


