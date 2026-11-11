from contextlib import redirect_stdout
from io import StringIO

from django.test import TestCase
from django.urls import reverse

from populate_db import populate_products

from .models import Product


class CashRegisterViewTests(TestCase):
    def setUp(self):
        self.product = Product.objects.create(
            upc_code='123456789012',
            name='Demo Product',
            price='10.99',
        )

    def test_get_displays_the_lookup_form(self):
        response = self.client.get(reverse('cash_register'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Enter UPC Code')

    def test_valid_upc_displays_the_matching_product(self):
        response = self.client.post(
            reverse('cash_register'),
            {'upc_code': self.product.upc_code},
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.product.name)
        self.assertContains(response, '10.99')

    def test_invalid_upc_returns_a_validation_message(self):
        response = self.client.post(
            reverse('cash_register'),
            {'upc_code': 'not-a-upc'},
        )

        self.assertEqual(response.status_code, 400)
        self.assertContains(
            response,
            'Enter a 12-digit UPC code.',
            status_code=400,
        )

    def test_unknown_upc_returns_a_not_found_message(self):
        response = self.client.post(
            reverse('cash_register'),
            {'upc_code': '999999999999'},
        )

        self.assertEqual(response.status_code, 404)
        self.assertContains(
            response,
            'No product was found for that UPC code.',
            status_code=404,
        )

    def test_seed_script_can_run_more_than_once(self):
        Product.objects.all().delete()

        with redirect_stdout(StringIO()):
            populate_products()
            populate_products()

        self.assertEqual(Product.objects.count(), 3)
