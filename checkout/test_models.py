# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from decimal import Decimal
from django.test import TestCase

# Internal:
from products.models import Product
from rugby_shop import settings
from .models import Order
from .models import OrderLineItem
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class TestCheckoutModels(TestCase):
    """
    A class for testing checkout models
    """
    def setUp(self):
        """
        Create a test product and order
        """
        Product.objects.create(
            name='Test Name',
            price='99.99',
            colour='Test Colour',
            code='123456',
            description='Test Description',
        )

        Order.objects.create(
            full_name='Test Name',
            email='test@gmail.com',
            phone_number='123456789',
            country='IE',
            town_or_city='Test City',
            street_address1='Test Address',
        )

    def tearDown(self):
        """
        Delete test products and orders
        """
        Product.objects.all().delete()
        Order.objects.all().delete()

    def test_order_str_method(self):
        """
        This test tests the order number string
        """
        order = Order.objects.get(email='test@gmail.com')
        self.assertEqual(str(order), order.order_number)
