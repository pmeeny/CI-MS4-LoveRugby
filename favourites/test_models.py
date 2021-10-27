from django.contrib.auth.models import User
from django.test import TestCase

from favourites.models import Favourites
from products.models import Product


class TestNewsModels(TestCase):
    def setUp(self):

        test_user = User.objects.create_user(
            username='test_user', password='test_password')

        product = Product.objects.create(
            name='Test Name',
            price='99.99',
            colour='Test Colour',
            code='123456',
            description='Test Description',
        )

        Favourites.objects.create(
            username=test_user
        )

    def test_favourites_str_method(self):
        """
        This test tests the favourites str method
        """
        favourite = Favourites.objects.get()
        self.assertEqual((favourite.__str__()), "test_user's Favourites")

