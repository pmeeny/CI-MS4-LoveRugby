
from django.test import TestCase
from django.contrib.messages import get_messages

from django.contrib.auth.models import User
from products.models import Product
from checkout.models import Order
from profiles.models import UserProfile


class TestProfileViews(TestCase):

    def setUp(self):
        testuser = User.objects.create_user(
            username='joebloggs',
            password='password123',
            email='test@email.com')
        testuser.save()

        #testuser_2 = User.objects.create_user(
        ##    username='testuser2',
        #    password='testpassword',
        #    email='test@email.com')
        #testuser_2.save()

        testuser_profile = UserProfile.objects.get(user=testuser)

        Product.objects.create(
            name='Test Title',
            code='Test SKU',
            price='1',
        )

        Order.objects.create(
            order_number='TestOrder1',
            user_profile=testuser_profile,
            full_name='Joebloggs',
            email='joebloggs@email.com',
            phone_number='0871234567',
            country='IE',
            postcode='test postcode',
            town_or_city='test city',
            street_address1='test address 1',
            county='test country',
        )

    # Test Profile View
    #
    def test_get_profile_page(self):
        self.client.login(username='joebloggs', password='password123')
        response = self.client.get('/profile/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/profile.html')