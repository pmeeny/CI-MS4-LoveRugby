from django.test import TestCase
from django.contrib.messages import get_messages

from django.contrib.auth.models import User
from checkout.models import Order
from profiles.models import UserProfile


class TestCheckoutViews(TestCase):

    def setUp(self):
        test_user = User.objects.create_user(
            username='test_user', password='test_password')
        test_user_superuser = User.objects.create_superuser(
            username='test_user_superuser', password='test_password')

        test_user.save()
        test_user_superuser.save()

        test_user = UserProfile.objects.get(user=test_user)

        Order.objects.create(
            full_name='Test User',
            email='test_email@gmail.com',
            phone_number='123456789',
            country='IE',
            town_or_city='Test City',
            street_address1='Test Address 1',
            street_address2 = 'Test Address 2',
            user_profile=test_user
        )

    def test_checkout_view_empty_cart(self):
        """
        This test test an empty cart for checkout
        """
        response = self.client.get('/checkout/')
        self.assertRedirects(response, '/products/')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(
            str(messages[0]), "There's nothing in your bag at the moment")

