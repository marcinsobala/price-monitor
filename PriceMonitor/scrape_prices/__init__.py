shop_xpaths = {'123lazienka.pl':
                   {'name': '//meta[@property="og:title"]/@content',
                    'price': '//span[@itemprop="price"]/text()',
                    'currency': '//meta[@itemprop="priceCurrency"]/@content'},
               '3xk.pl':
                   {'name': '//meta[@property="og:title"]/@content',
                    'price': '//strong[@id="projector_price_value"]/text()',
                    'currency': '//meta[@property="og:title"]/@content'},
               'agdmaster.com':
                   {'name': '//div[@id="product-description"]/div/h1/text()',
                    'price': '//p[@class="lead price selling"]/text()',
                    'currency': '//div[@id="product-description"]/div/h1/text()'},
               'aleplanszowki.pl':
                   {'name': '//meta[@property="og:title"]/@content',
                    'price': '//span[@itemprop="price"]/text()',
                    'currency': '//meta[@itemprop="priceCurrency"]/@content'},
               'allegro.pl':
                   {'name': '//meta[@property="og:title"]/@content',
                    'price': '//meta[@itemprop="price"]/@content',
                    'currency': '//meta[@itemprop="priceCurrency"]/@content'},
               'am76.pl':
                   {'name': '//meta[@itemprop="name"]/@content',
                    'price': '//meta[@itemprop="price"]/@content',
                    'currency': '//meta[@itemprop="priceCurrency"]/@content'},
               'aptekagemini.pl':
                   {'name': '//h1[@itemprop="name"]/text()',
                    'price': '//meta[@itemprop="price"]/@content',
                    'currency': '//meta[@itemprop="priceCurrency"]/@content'},
               'apteka-melissa.pl':
                   {'name': '//h1[@class="roboto h1-karta-produktu"]/text()',
                    'price': '//h2[contains(@class, "roboto cena_pro")]//text()[2]',
                    'currency': '//span[@itemprop="priceCurrency"]/text()'},
               'aros.pl':
                   {'name': '//meta[@property="og:title"]/@content',
                    'price': '//meta[@itemprop="price"]/@content',
                    'currency': '//meta[@itemprop="currency"]/@content'},
               'bezokularow.pl':
                   {'name': '//h1[@itemprop="name"]/text()',
                    'price': '//span[@id="yp"]/text()',
                    'currency': '//span[@id="yp"]/span/text()'},
               'bonito.pl':
                   {'name': '//meta[@property="og:title"]/@content',
                    'price': '//meta[@itemprop="price"]/@content',
                    'currency': '//meta[@itemprop="currency"]/@content'},
               'brw.pl':
                   {'name': '//h1[@property="name"]/text()',
                    'price': '//div[@itemprop="price"]/@content',
                    'currency': '//meta[@itemprop="priceCurrency"]/@content'},
               'ceneo.pl':
                   {'name': '//meta[@property="og:title"]/@content',
                    'price': '//meta[@property="product:price:amount"]/@content',
                    'currency': '//meta[@property="product:price:currency"]/@content'},
               'congee.pl':
                   {'name': '//meta[@property="og:title"]/@content',
                    'price': '//meta[@itemprop="price"]/@content',
                    'currency': '//meta[@itemprop="priceCurrency"]/@content'},
               'cqb.pl':
                   {'name': '//meta[@name="Description"]/@content',
                    'price': '//div[@id="cena_produktu"]/span[1]/text()',
                    'currency': '//meta[@name="Description"]/@content'},
               'decathlon.pl':
                   {'name': '//span[@id="productName"]/text()',
                    'price': '//meta[@property="og:description"]/@content',
                    'currency': '//span[@class="currency minus spacing"]/text()'},
               'diabetyk24.pl':
                   {'name': '//h1[@class="product-title"]/text()',
                    'price': '//span[@class="product-price-current"]/strong/text()',
                    'currency': '//h1[@class="product-title"]/text()'},
               'dragonus.pl':
                   {'name': '//meta[@name="og:title"]/@content',
                    'price': '//div[@class="price"]/em/text()',
                    'currency': '//div[@class="currency none"]/text()'},
               'edugaleria.pl':
                   {'name': '//h1[@class="tytulB2C"]/span/text()',
                    'price': '//meta[@name="description"]/@content',
                    'currency': '//meta[@itemprop="priceCurrency"]/@content'},
               'empik.com':
                   {'name': '//meta[@property="og:title"]/@content',
                    'price': '//span[@itemprop="price"]/@content',
                    'currency': '//span[@itemprop="priceCurrency"]/@content'},
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
               'fera.pl':
                   {'name': '//meta[@property="og:title"]/@content',
                    'price': '//meta[@property="product:price:amount"]/@content',
                    'currency': '//meta[@property="product:price:currency"]/@content'},
               'gmoto.pl':
                   {'name': '//meta[@property="og:title"]/@content',
                    'price': '//meta[@name="Description"]/@content',
                    'currency': '//span[@itemprop="priceCurrency"]/text()'},
               'gryplanszowe.pl':
                   {'name': '//meta[@property="og:title"]/@content',
                    'price': '//strong[@id="projector_price_value"]/text()',
                    'currency': '//strong[@id="projector_price_value"]/text()'},
               'gunfire.com':
                   {'name': '//meta[@property="og:title"]/@content',
                    'price': '//span[@id="projector_price_srp"]/text()',
                    'currency': '//span[@class="menu_settings_barval"]/text()'},
               'jeans24h.pl':
                   {'name': '//div[@class="headcorners"]/h1/text()',
                    'price': '//meta[@itemprop="price"]/@content',
                    'currency': '//meta[@itemprop="currency"]/@content'},
               'krakvet.pl':
                   {'name': '//meta[@property="og:title"]/@content',
                    'price': '//strong[@id="projector_price_value"]/text()',
                    'currency': '//strong[@id="projector_price_value"]/text()'},
               'kucmar.pl':
                   {'name': '//meta[@property="og:title"]/@content',
                    'price': '//meta[@itemprop="price"]/@content',
                    'currency': '//meta[@itemprop="priceCurrency"]/@content'},
               'manada.pl':
                   {'name': '//span[@itemprop="name"]/text()',
                    'price': '//meta[@itemprop="price"]/@content',
                    'currency': '//meta[@itemprop="currency"]/@content'},
               'manito.pl':
                   {'name': '//meta[@property="og:title"]/@content',
                    'price': '//strong[@id="projector_price_value"]/text()',
                    'currency': '//span[@class="menu_settings_currency"]/text()'},
               'morele.net':
                   {'name': '//*[@itemtype="http://schema.org/AggregateRating"]/div/span[@itemprop="name"]/text()',
                    'price': '//div[@itemprop="price"]/@content',
                    'currency': '//div[@ itemprop="priceCurrency"]/@content'},
               'nestof.pl':
                   {'name': '//meta[@property="og:title"]/@content',
                    'price': '//strong[@id="projector_price_value"]/text()',
                    'currency': '//meta[@property="og:title"]/@content'},
               'north.pl':
                   {'name': '//meta[@property="og:title"]/@content',
                    'price': '//meta[@property="og:price:amount"]/@content',
                    'currency': '//meta[@property="og:price:currency"]/@content'},
               'olx.pl':
                   {'name': '//meta[@property="og:title"]/@content',
                    'price': '//strong[@class="xxxx-large not-arranged"]/text()',
                    'currency': '//meta[@property="og:title"]/@content'},
               'pieknowdomu.pl':
                   {'name': '//h1[@class="product-main-header"]/text()',
                    'price': '//div[@itemprop="offers"]/descendant::span[@itemprop="price"]/@content',
                    'currency': '//meta[@itemprop="priceCurrency"]/@content'},
               'porcelana24.pl':
                   {'name': '//h1[@itemprop="name"]/text()',
                    'price': '//meta[@itemprop="price"]/@content',
                    'currency': '//meta[@itemprop="priceCurrency"]/@content'},
               'sfd.pl':
                   {'name': '//h1[@itemprop="name"]/text()[2]',
                    'price': '//span[@itemprop="price"]/@content',
                    'currency': '//meta[@itemprop="priceCurrency"]/@content'},
               'swiatksiazki.pl':
                   {'name': '//meta[@property="og:title"]/@content',
                    'price': '//meta[@property="product:price:amount"]/@content',
                    'currency': '//meta[@property="product:price:currency"]/@content'},
               'taniaksiazka.pl':
                   {'name': '//meta[@itemprop="name"]/@content',
                    'price': '//meta[@itemprop="price"]/@content',
                    'currency': '//meta[@itemprop="priceCurrency"]/@content'},
               'telekarma.pl':
                   {'name': '//div[@id="productCard"]/h1/text()',
                    'price': '//span[@class="productCardPrice-price"]/text()',
                    'currency': '//div[@id="productCard"]/h1/text()'},
               'wapteka.pl':
                   {'name': '//meta[@property="og:title"]/@content',
                    'price': '//meta[@itemprop="price"]/@content',
                    'currency': '//meta[@itemprop="priceCurrency"]/@content'},
               'wideshop.pl':
                   {'name': '//meta[@property="og:title"]/@content',
                    'price': '//strong[@id="projector_price_value"]/text()',
                    'currency': '//span[@class="menu_settings_currency"]/text()'},
               'wittchen.com':
                   {'name': '//meta[@property="og:title"]/@content',
                    'price': '//span[@itemprop="price"]/text()',
                    'currency': '//meta[@itemprop="priceCurrency"]/@content'},
               'x-kom.pl':
                   {'name': '//meta[@property="og:title"]/@content',
                    'price': '//meta[@property="product:price:amount"]/@content',
                    'currency': '//meta[@property="product:price:currency"]/@content'},
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
                    'currency': '//meta[@property="og:title"]/@content'},
               'zooplus.pl':
                   {'name': '//meta[@property="og:title"]/@content',
                    'price': '//meta[@itemprop="price"]/@content',
                    'currency': '//meta[@itemprop="priceCurrency"]/@content'}
               }
