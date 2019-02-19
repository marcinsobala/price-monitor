import requests
from lxml import html

# Returns url content in html format
def get_html_content(url):
    pageContent = requests.get(url)
    return html.fromstring(pageContent.content)


# Imports url set from SQL database
urls = {'https://allegro.pl/oferta/gigabyte-geforce-rtx-2070-windforce-8g-8gb-gddr6-7820820756',
        'https://www.ceneo.pl/71356120',
        'https://www.morele.net/karta-graficzna-gigabyte-geforce-rtx-2070-windforce-8g-8gb-gddr6-256-bit-3xhdmi-3xdp'
        '-usb-c-box-gv-n2070wf3-8gc-4142730/',
        'https://www.zalando.pl/pier-one-bluza-rozpinana-black-pi922s028-q11.html'
        }


def name_price_currency(url):
    tree = get_html_content(url)
    if "allegro.pl" in url:
        name = tree.xpath('//div[@ itemtype="http://schema.org/Product"]/meta[@ itemprop="name"]/@content')
        price = tree.xpath('//div[@ itemtype="http://schema.org/Offer"]/meta[@ itemprop="price"]/@content')
        currency = tree.xpath('//div[@ itemtype="http://schema.org/Offer"]/meta[@ itemprop="priceCurrency"]/@content')

    elif "ceneo.pl" in url:
        name = tree.xpath('//div[@ itemtype="http://schema.org/Product"]/meta[@ itemprop="name"]/@content')
        price = tree.xpath('//div[@ itemtype="http://schema.org/Offer"]/meta[@ itemprop="price"]/@content')
        currency = tree.xpath('//div[@ itemtype="http://schema.org/Offer"]/meta[@ itemprop="priceCurrency"]/@content')

    elif "morele.net" in url:
        name = tree.xpath('//*[@ itemtype="http://schema.org/AggregateRating"]/div/span[@ itemprop="name"]/text()')
        price = tree.xpath('//div[@ itemprop="price"]/@content')
        currency = tree.xpath('//div[@ itemprop="priceCurrency"]/@content')

    elif "zalando.pl" in url:
        name = tree.xpath('//div[@ itemtype="http://schema.org/Product"]/meta[@ itemprop="name"]/@content')
        price = tree.xpath('//div[@ itemtype="http://schema.org/Offer"]/meta[@ itemprop="price"]/@content')
        currency = tree.xpath('//div[@ itemtype="http://schema.org/Offer"]/meta[@ itemprop="priceCurrency"]/@content')


    return (name[0], price[0], currency[0])


# print(name_price_currency('https://www.morele.net/karta-graficzna-gigabyte-geforce-rtx-2070-windforce-8g-8gb-gddr6-256-bit-3xhdmi-3xdp'
#         '-usb-c-box-gv-n2070wf3-8gc-4142730/'))

# # Loops through urls and prints the product prices
# for url in urls:
#     tree = get_html_content(url)
#
#     # looks for price in different html locations depending on site address
#     if "allegro.pl" in url:
#         itemData = tree.xpath('//div[@ itemtype="http://schema.org/Offer"]/meta[@ itemprop="price"]/@content')
#     elif "ceneo.pl" in url:
#         itemData = tree.xpath('//span[@ class="offer-summary"]/a[1]/@data-lowestprice')
#     elif "morele.net" in url:
#         itemData = tree.xpath('//div[@ itemprop="price"]/@content')
#     elif "zalando.pl" in url:
#         itemData = tree.xpath('//div[@ class="h-product-price h-m-bottom-xl topSection"]/div[1]/text()')
#
#     print(itemData[0].replace(',', '.'))

# Algorithm first draft
#
# def get_urls():
#     dict = {'www.google.pl': (100, 200, 123450, 123456, 12.05.12)}
#     return
#
#
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
