# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.contrib.auth.models import User
from django.test import TestCase

# Internal:
from favourites.models import Favourites
from products.models import Product

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class TestFavouriteModels(TestCase):
    """
    A class for testing favourites models
    """
    def setUp(self):
        """
        Create test users, product and favourite
        """
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

    def tearDown(self):
        """
        Delete test user, product and favourite
        """
        User.objects.all().delete()
        Product.objects.all().delete()
        Favourites.objects.all().delete()

    def test_favourites_str_method(self):
        """
        This test tests the favourites str method
        """
        favourite = Favourites.objects.get()
        self.assertEqual((favourite.__str__()), "test_user's Favourites")
