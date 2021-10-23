from django.contrib.messages import get_messages
from django.test import TestCase

from products.models import Product


class TestBagViews(TestCase):

    def setUp(self):
        Product.objects.create(
            name='Test Name',
            price='19.99',
            colour='Test Colour',
            code='123456',
        )

    def test_get_bag_page(self):
        """
        This test checks that the bag page
        is displayed
        """
        response = self.client.get('/bag/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bag/bag.html')

    def test_add_to_empty_bag_no_size(self):
        """
        This test adds a product with no size to an empty bag
        """
        product = Product.objects.get(code='123456')
        response = self.client.post(f'/bag/add/{product.id}/',
                                    {"quantity": 1, "redirect_url": "view_bag"})
        bag = self.client.session['bag']
        self.assertEqual(bag[str(product.id)], 1)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]), 'Added Test Name to your bag')

    def test_add_to_empty_bag_with_size(self):
        """
        This test adds a product with a size to an empty bag
        """
        product = Product.objects.get(code='123456')
        response = self.client.post(f'/bag/add/{product.id}/',
                                    {"quantity": 1, "redirect_url": "view_bag", "product_size": 1})
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]), 'Added size 1 Test Name to your bag')

    def test_adjust_bag_quantity_to_two(self):
        """
        This test updates a products quantity to 2
        """
        product = Product.objects.get(code='123456')
        response = self.client.post(f'/bag/adjust/{product.id}/', {
            'quantity': 2
        })
        bag = self.client.session['bag']
        self.assertEqual(bag[str(product.id)], 2)
        messages = list(get_messages(response.wsgi_request))
        product_id = bag[str(product.id)]
        self.assertEqual(str(messages[0]), 'Updated Test Name quantity to ' + str(product_id))

    def test_adjust_bag_quantity_to_zero(self):
        """
        This test reduces the bag from 1 item to 0 items
        """
        product = Product.objects.get(code='123456')
        response = self.client.post(f'/bag/add/{product.id}/', {
            'quantity': 1, "redirect_url": "view_bag",
        })
        self.assertRedirects(response, '/bag/')
        bag = self.client.session['bag']
        self.assertEqual(bag[str(product.id)], 1)
        response = self.client.post(f'/bag/adjust/{product.id}/', {
            'quantity': 0, "redirect_url": "view_bag",
        })
        self.assertRedirects(response, '/bag/')
        bag = self.client.session['bag']
        self.assertEqual(bag, {})
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]), 'Removed Test Name from your bag')

    def test_remove_product_from_bag(self):
        """
        This test removes a product from the bag
        """
        product = Product.objects.get(code='123456')
        self.client.post(f'/bag/add/{product.id}/', {
            'quantity': 1, "redirect_url": "view_bag"
        })
        bag = self.client.session['bag']
        self.assertEqual(bag[str(product.id)], 1)
        response = self.client.post(f'/bag/remove/{product.id}/')
        bag = self.client.session['bag']
        self.assertEqual(bag, {})
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[1]), 'Removed Test Name from your bag')

    def test_remove_product_from_bag_with_size(self):
        """
        This test removes a product with a size from the bag
        """
        product = Product.objects.get(code='123456')
        self.client.post(f'/bag/add/{product.id}/', {
            'quantity': 1, "redirect_url": "view_bag", "product_size": 1
        })
        response = self.client.post(f'/bag/remove/{product.id}/',
                                    {"product_size": 1})
        bag = self.client.session['bag']
        self.assertEqual(bag, {})
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[1]), 'Removed size 1 Test Name from your bag')

    def test_remove_product_from_bag_exception(self):
        """
        This test tries to remove a product from a bag
        that doesnt exist, and an exception is thrown
        """
        product = Product.objects.get(code='123456')
        response = self.client.post(f'/bag/remove/{product.id}/')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]), "Error removing item: '1'")
