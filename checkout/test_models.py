from decimal import Decimal
from django.test import TestCase

from products.models import Product
from rugby_shop import settings
from .models import Order
from .models import OrderLineItem


class TestCheckoutModels(TestCase):
    def setUp(self):
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

    def test_order_str_method(self):
        order = Order.objects.get(email='test@gmail.com')
        self.assertEqual(str(order), order.order_number)
        
    def test_order_with_delivery(self):
        order = Order.objects.get(email='test@gmail.com')
        product = Product.objects.get(code='123456')
        order_line_item = OrderLineItem.objects.create(
            order=order,
            product=product,
            quantity=1,
        )
        self.assertEqual(
            order_line_item.lineitem_total, Decimal(
                order_line_item.product.price * order_line_item.quantity)
        )
        self.assertEqual(order.delivery_cost, settings.STANDARD_DELIVERY_PERCENTAGE)
