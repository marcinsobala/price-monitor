shop_xpaths = {'allegro.pl':
                   {'name': '//meta[@property="og:title"]/@content',
                    'price': '//meta[@itemprop="price"]/@content',
                    'currency': '//meta[@itemprop="priceCurrency"]/@content'},
               'apteka-melissa.pl':
                   {'name': '//h1[@class="roboto h1-karta-produktu"]/text()',
                    'price': '//h2[contains(@class, "roboto cena_pro")]//text()[2]',
                    'currency': '//span[@itemprop="priceCurrency"]/text()'},
               'ceneo.pl':
                   {'name': '//meta[@property="og:title"]/@content',
                    'price': '//meta[@property="product:price:amount"]/@content',
                    'currency': '//meta[@property="product:price:currency"]/@content'},
               'eobuwie.com.pl':
                   {'name': '//meta[@property="og:title"]/@content',
                    'price': '//meta[@property="product:price:amount"]/@content',
                    'currency': '//meta[@property="product:price:currency"]/@content'},
               'jeans24h.pl':
                   {'name': '//div[@class="headcorners"]/h1/text()',
                    'price': '//meta[@itemprop="price"]/@content',
                    'currency': '//meta[@itemprop="currency"]/@content'},
               'morele.net':
                   {'name': '//*[@itemtype="http://schema.org/AggregateRating"]/div/span[@itemprop="name"]/text()',
                    'price': '//div[@itemprop="price"]/@content',
                    'currency': '//div[@ itemprop="priceCurrency"]/@content'},
               'north.pl':
                   {'name': '//meta[@property="og:title"]/@content',
                    'price': '//meta[@property="og:price:amount"]/@content',
                    'currency': '//meta[@property="og:price:currency"]/@content'},
               'olx.pl':
                   {'name': '//meta[@property="og:title"]/@content',
                    'price': '//strong[@class="xxxx-large not-arranged"]/text()',
                    'currency': '//meta[@property="og:title"]/@content'},
               'zalando.pl':
                   {'name': '//meta[@property="og:title"]/@content',
                    'price': '//meta[@name="twitter:data1"]/@content',
                    'currency': '//meta[@name="twitter:data1"]/@content'}}
