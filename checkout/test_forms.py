from django.test import TestCase

from .forms import OrderForm
from .models import Order


class TestCheckoutForms(TestCase):

    def test_add_order_form(self):
        form = OrderForm({
            'full_name': 'Test Name',
            'email': 'test@gmail.com',
            'phone_number': '123456789',
            'street_address1': 'Test Address 1',

            })
        self.assertTrue(form.is_valid())
        form.save()
        Order.objects.get(full_name='Test Name')
        Order.objects.get(email='test@gmail.com')
        Order.objects.get(country='Test Country')
