from django.test import TestCase
from tracked_prices.models import Shop


class TestShop(TestCase):
    def setUp(self):
        Shop.objects.create(
            url="https://allegro.pl/",
            name='allegro'
        )

    def test_dunder_str_returns_just_name(self):
        allegro = Shop.objects.get(name='allegro')
        print(allegro.__str__())
        self.assertEqual(allegro.__str__(), 'allegro.pl')
