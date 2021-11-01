from django.test import TestCase

from .forms import OrderForm


class TestCheckoutForms(TestCase):

    def test_add_order_form(self):
        """
        This test tests the order form object
        """
        form = OrderForm({
            'full_name': 'test name',
            'email': 'test@email.com',
            'phone_number': '123456',
            'country': 'IE',
            'town_or_city': 'test city',
            'street_address1': 'test address 1',
            'street_address2': 'test address 2',
            })
        self.assertTrue(form.is_valid())
