from django.test import TestCase
from .models import Product


class ProductTest(TestCase):
    """Here we will define the tests that we will run against our Product models"""

    def test_str(self):
        test_name = Product(name='A product')
        self.assertEqual(str(test_name), 'A product')
