from django.contrib.auth.models import User
from django.contrib.messages import get_messages
from django.test import TestCase

from favourites.models import Favourites
from products.models import Product


class TestFavouritesViews(TestCase):
    def setUp(self):
        test_user = User.objects.create_user(
            username='test_user', password='test_password')

        Favourites.objects.create(
            username=test_user
        )

    def test_get_product_favourites_page(self):
        """
        This test tests get the product favourites page
        """
        self.client.login(username='test_user', password='test_password')
        response = self.client.get('/favourites/view_product_favourites/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'favourites/favourites.html')

    def test_get_product_favourites_empty_list(self):
        """
        This test tests an empty product favourites list
        """
        self.client.login(username='test_user', password='test_password')
        response = self.client.get('/favourites/view_product_favourites/')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]), "Your favourites list is empty!")

    def test_add_item_to_product_favourites(self):
        """
        This test adds a product to the users favourites list
        """
        self.client.login(username='test_user', password='test_password')
        product = Product.objects.create(
            name='Test Name',
            price='99.99',
            colour='Test Colour',
            code='123456',
            description='Test Description',
        )
        response = self.client.post(f'/favourites/add_product_to_favourites/'
                                    f'{product.id}/')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]), "Added product item "
                                           "to your favourites")

    def test_add_item_already_in_product_favourites(self):
        """
        This test adds a product to the users favourites list
        that already exists
        """
        self.client.login(username='test_user', password='test_password')
        product = Product.objects.create(
            name='Test Name 1',
            price='99.99',
            colour='Test Colour',
            code='123456',
            description='Test Description',
        )
        response = self.client.post(f'/favourites/add_product_to_favourites/'
                                    f'{product.id}/')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]), "Added product item "
                                           "to your favourites")
        response = self.client.post(f'/favourites/add_product_to_favourites/'
                                    f'{product.id}/')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[1]), 'The product item is already '
                                           'in your favourites!')

    def test_remove_item_from_favourites_redirect_favourites(self):
        """
        This test removes a product from the users favourites list
        with a redirect back to the favourites page
        """
        test_user1 = User.objects.create_user(
            username='test_user1', password='test_password')
        self.client.login(username='test_user1', password='test_password')
        test_user1 = User.objects.get(username='test_user1')
        product = Product.objects.create(
            name='Test Name 2',
            price='99.99',
            colour='Test Colour',
            code='123456',
            description='Test Description',
        )
        product = Product.objects.get(name='Test Name 2')
        favourites = Favourites.objects.create(username=test_user1)
        favourites.products.add(product)
        redirect_from = 'favourites'
        response = self.client.get(
            f'/favourites/remove_product_from_favourites/'
            f'{product.id}/{redirect_from}/')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]), 'Product item removed '
                                           'from your favourites list')

    def test_remove_item_from_favourites_redirect_product(self):
        """
        This test removes a product from the users favourites list
        with a redirect back to the products page
        """
        test_user1 = User.objects.create_user(
            username='test_user1', password='test_password')
        self.client.login(username='test_user1', password='test_password')
        test_user1 = User.objects.get(username='test_user1')
        product = Product.objects.create(
            name='Test Name 2',
            price='99.99',
            colour='Test Colour',
            code='123456',
            description='Test Description',
        )
        product = Product.objects.get(name='Test Name 2')
        favourites = Favourites.objects.create(username=test_user1)
        favourites.products.add(product)
        redirect_from = 'product'
        response = self.client.get(
            f'/favourites/remove_product_from_favourites/'
            f'{product.id}/{redirect_from}/')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]), 'Product item removed '
                                           'from your favourites list')

    def test_remove_item_not_in_favourites(self):
        """
        This test attempts to remove a product that does not exist in the
        users favourites list
        """
        test_user1 = User.objects.create_user(
            username='test_user1', password='test_password')
        self.client.login(username='test_user1', password='test_password')
        test_user1 = User.objects.get(username='test_user1')
        product = Product.objects.create(
            name='Test Name 2',
            price='99.99',
            colour='Test Colour',
            code='123456',
            description='Test Description',
        )
        product = Product.objects.get(name='Test Name 2')
        Favourites.objects.create(username=test_user1)
        redirect_from = 'product'
        response = self.client.get(
            f'/favourites/remove_product_from_favourites/'
            f'{product.id}/{redirect_from}/')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]), 'That product item is not in '
                                           'your favourites list!')
