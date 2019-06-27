shop_xpaths = {'allegro.pl':
                   {'name': '//meta[@property="og:title"]/@content',
                    'price': '//meta[@itemprop="price"]/@content',
                    'currency': '//meta[@itemprop="priceCurrency"]/@content'},
               'ceneo.pl':
                   {'name': '//meta[@property="og:title"]/@content',
                    'price': '//meta[@property="og:price:amount"]/@content',
                    'currency': '//meta[@property="og:price:currency"]/@content'},
               'jeans24h.pl':
                   {'name': '//div[@class="headcorners"]/h1/text()',
                    'price': '//meta[@itemprop="price"]/@content',
                    'currency': '//meta[@itemprop="currency"]/@content'},
               'morele.net':
                   {'name': '//*[@itemtype="http://schema.org/AggregateRating"]/div/span[@itemprop="name"]/text()',
                    'price': '//div[@itemprop="price"]/@content',
                    'currency': '//div[@ itemprop="priceCurrency"]/@content'},
               'zalando.pl':
                   {'name': '//meta[@property="og:title"]/@content',
                    'price': '//meta[@name="twitter:data1"]/@content',
                    'currency': '//meta[@name="twitter:data1"]/@content'}}
