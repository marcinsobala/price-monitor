from django.test import TestCase
from tracked_prices.models import TrackedPrice


class TestTrackedPrice(TestCase):
    def setUp(self):
        TrackedPrice.objects.create(
            name='product1',
            url=(
                'https://allegro.pl/oferta/konsola-ps3-classic-nowy-pad-gta-5'
                '-cod-dzieci-3gry-8505568684?bi_s=ads&bi_m=listing%3Adesktop%3Aquery&bi'
                '_c=YTdkZjhiODctYjk0ZS00NmJjLWFlN2UtMjg4NjYzZTlkMzlkAA&bi_t=ape&referrer'
                '=proxy&emission_unit_id=551d3c88-d19a-4098-96a1-206cd7bb1294'))

    def test_dunder_str_returns_just_shop_name(self):
        product1 = TrackedPrice.objects.get(name='product1')

        self.assertEqual(product1.__str__, 'allegro.pl')
