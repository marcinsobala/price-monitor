import requests, re
from lxml import html

# Following 4 lines enable scrape.py to use Django ORM
import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PriceMonitor.settings')
from django.conf import settings
django.setup()

from django.utils import timezone
from django.core.mail import send_mail
from tracked_prices.models import TrackedPrice
from django.contrib.auth.models import User
from operator import itemgetter


def get_html_content(url):
    pageContent = requests.get(url)
    return html.fromstring(pageContent.content)

# TODO - is currency necessary? May need to regex jsons to get it / Dict, not if elif
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

# TODO - dict, not if elif
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


# Returns query set of all necessary tracked price data
def tracked_price_data():
    return TrackedPrice.objects.values('id', 'user_id', 'when_inform', 'current',
                                       'desired', 'percent_drop', 'url')


# TODO Multithreading!
# Updates prices current value and last checked date but checks only unique urls
def update_current_prices():
    unique_urls = TrackedPrice.objects.values_list('url').distinct()
    scraped_prices = ({'url': url[0], 'current': get_price(url[0])} for url in unique_urls)
    for scraped_price in scraped_prices:
        TrackedPrice.objects \
            .filter(url=scraped_price['url']) \
            .update(current=scraped_price['current'],
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
        message = f"Cena {price.name} spadła do {price.current} {price.currency}!\n"

        # Appends to previous message if it's the price belonging to the same user,
        # otherwise creates a new message
        if user_id != previous_user_id:
            user = User.objects.get (id=user_id)
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


def send_mails(prepared_emails):
    email_from = settings.EMAIL_HOST_USER
    password = settings.EMAIL_HOST_PASSWORD
    for message in prepared_emails:
        send_mail(message['subject'],
                  message['message'],
                  message['email'],
                  recipient_list=[email_from],
                  auth_password=password)


# updates prices and sends out emails if prices are now satisfactory for the user
def price_drop_inform():
    old_prices = list(tracked_price_data())
    update_current_prices()
    prices_users_IDs = is_price_satisfactory(old_prices)

    # No point in running these functions if no prices are satisfactory
    if prices_users_IDs:
        prepared_emails = prepare_emails(prices_users_IDs)
        send_mails(prepared_emails)




