shop_xpaths = {'123lazienka.pl':
                   {'name': '//meta[@property="og:title"]/@content',
                    'price': '//span[@itemprop="price"]/text()',
                    'currency': '//meta[@itemprop="priceCurrency"]/@content'},
               'aleplanszowki.pl':
                   {'name': '//meta[@property="og:title"]/@content',
                    'price': '//span[@itemprop="price"]/text()',
                    'currency': '//meta[@itemprop="priceCurrency"]/@content'},
               'allegro.pl':
                   {'name': '//meta[@property="og:title"]/@content',
                    'price': '//meta[@itemprop="price"]/@content',
                    'currency': '//meta[@itemprop="priceCurrency"]/@content'},
               'apteka-melissa.pl':
                   {'name': '//h1[@class="roboto h1-karta-produktu"]/text()',
                    'price': '//h2[contains(@class, "roboto cena_pro")]//text()[2]',
                    'currency': '//span[@itemprop="priceCurrency"]/text()'},
               'bonito.pl':
                   {'name': '//meta[@property="og:title"]/@content',
                    'price': '//meta[@itemprop="price"]/@content',
                    'currency': '//meta[@itemprop="currency"]/@content'},
               'ceneo.pl':
                   {'name': '//meta[@property="og:title"]/@content',
                    'price': '//meta[@property="product:price:amount"]/@content',
                    'currency': '//meta[@property="product:price:currency"]/@content'},
               'decathlon.pl':
                   {'name': '//span[@id="productName"]/text()',
                    'price': '//meta[@property="og:description"]/@content',
                    'currency': '//span[@class="currency minus spacing"]/text()'},
               'eobuwie.com.pl':
                   {'name': '//meta[@property="og:title"]/@content',
                    'price': '//meta[@property="product:price:amount"]/@content',
                    'currency': '//meta[@property="product:price:currency"]/@content'},
               'etuo.pl':
                   {'name': '//meta[@name="keywords"]/@content',
                    'price': '//span[@itemprop="price"]/@content',
                    'currency': '//meta[@itemprop="priceCurrency"]/@content'},
               'feedo.pl':
                   {'name': '//meta[@property="og:title"]/@content',
                    'price': '//meta[@itemprop="price"]/@content',
                    'currency': '//div[@id="fly-cart"]/@data-currency'},
               'gmoto.pl':
                   {'name': '//meta[@property="og:title"]/@content',
                    'price': '//meta[@name="Description"]/@content',
                    'currency': '//span[@itemprop="priceCurrency"]/text()'},
               'gunfire.com':
                   {'name': '//meta[@property="og:title"]/@content',
                    'price': '//span[@id="projector_price_srp"]/text()',
                    'currency': '//span[@class="menu_settings_barval"]/text()'},
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
               'sfd.pl':
                   {'name': '//h1[@itemprop="name"]/text()[2]',
                    'price': '//span[@itemprop="price"]/@content',
                    'currency': '//meta[@itemprop="priceCurrency"]/@content'},
               'zalando.pl':
                   {'name': '//meta[@property="og:title"]/@content',
                    'price': '//meta[@name="twitter:data1"]/@content',
                    'currency': '//meta[@name="twitter:data1"]/@content'},
               'zegarek.net':
                   {'name': '//meta[@name="keywords"]/@content',
                    'price': '//meta[@property="product:price:amount"]/@content',
                    'currency': '//meta[@property="product:price:currency"]/@content'},
               'zooart.com.pl':
                   {'name': '//meta[@property="og:title"]/@content',
                    'price': '//strong[@id="projector_price_value"]/text()',
                    'currency': '//meta[@property="og:title"]/@content'}
               }
