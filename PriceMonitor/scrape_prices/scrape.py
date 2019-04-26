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
# Following 3 lines enable module to use Django ORM  and app imports
# sys.path.append('..')
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PriceMonitor.PriceMonitor.settings')
# django.setup()

from django.conf import settings
from django.contrib.auth.models import User
from tracked_prices.models import TrackedPrice
from scrape_prices import shop_xpaths


async def get_html_content_async(url, session):
    async with session.get(url) as pageContent:
        return html.fromstring(await pageContent.text())


def get_html_content(url):
    try:
        return html.fromstring(requests.get(url).content)
    except requests.exceptions.RequestException:
        raise ConnectionError


def get_name_price_currency(url):
    tree = get_html_content(url)
    shop = re.search(r'https?://(www\.)?(\w+\.\w+)', url).group(2)

    name = tree.xpath(shop_xpaths[shop]['name'])[0]
    price = tree.xpath(shop_xpaths[shop]['price'])[0]
    currency = tree.xpath(shop_xpaths[shop]['currency'])[0]

    # Exceptions for websites which just can't store their metadata normally
    if shop == 'zalando.pl': currency = currency.split()[-1]

    price = re.search(r'\d+[.,]*\d*', price).group()
    price = re.sub(r',', '.', price)

    return name, price, currency


async def get_price(url, session, scraped_prices):
    tree = await get_html_content_async(url, session)
    shop = re.search (r'https?://(www\.)?(\w+\.\w+)', url).group (2)

    price = tree.xpath(shop_xpaths[shop]['price'])[0]
    price = re.search(r'\d+[.,]*\d*', price).group()
    price = re.sub(r',', '.', price)

    scraped_prices.append((url,price))


# Returns query set of all necessary tracked price data
def tracked_price_data():
    return TrackedPrice.objects.values('id', 'user_id', 'when_inform', 'current',
                                       'desired', 'percent_drop', 'url')


# Updates prices current value and last checked date but checks only unique urls
async def update_current_prices():
    unique_urls = TrackedPrice.objects.values_list('url').distinct().order_by('url')
    async with aiohttp.ClientSession() as session:
        tasks = []
        scraped_prices = []
        for url in unique_urls:
            task = asyncio.create_task(get_price(url[0], session, scraped_prices))
            tasks.append(task)
        await asyncio.gather(*tasks, return_exceptions=True)

    for price in scraped_prices:
        TrackedPrice.objects\
            .filter(url=price[0])\
            .update(current=price[1],
                     last_checked_date=timezone.now())

# Checks if prices dropped according to users wish and returns a list of tuples
# with prices id's and users id's sorted by users id's
def is_price_satisfactory(old_prices):
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


# Returns list of dictionaries with email addresses and prepared messages
def prepare_emails(prices_users_IDs):
    i = -1
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
            i += 1
            previous_user_id = user_id
        else:
            prepared_emails[i]['message'] += message

    for email in prepared_emails:
        email['message'] += 'Udanych zakupów, \nZespół Cebula Hunter'

    return prepared_emails


# TODO Secure password and mail
def send_mails(prepared_emails):
    for message in prepared_emails:
        send_mail(message['subject'],
                  message['message'],
                  settings.EMAIL_HOST_USER,
                  recipient_list=(message['email'],),
                  auth_password=settings.EMAIL_HOST_PASSWORD)


# updates prices and sends out emails if prices are now satisfactory for the user
def price_drop_inform():
    old_prices = list(tracked_price_data())
    asyncio.run(update_current_prices())
    prices_users_IDs = is_price_satisfactory(old_prices)

    # No point in running these functions if no prices are satisfactory
    if prices_users_IDs:
        prepared_emails = prepare_emails(prices_users_IDs)
        send_mails(prepared_emails)


if __name__ == "__main__":
    start_time = time.time()
    asyncio.run(update_current_prices())
    duration = time.time() - start_time
    print(duration)
    # print(get_name_price_currency('https://www.morele.net/karta-graficzna-gigabyte-geforce-rtx-2070-windforce-8g-8gb-gddr6-256-bit-3xhdmi-3xdp-usb-c-box-gv-n2070wf3-8gc-4142730/
