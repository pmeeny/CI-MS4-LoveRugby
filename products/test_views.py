from django.contrib.auth.models import User
from django.contrib.messages import get_messages
from django.test import TestCase

from products.models import Category, Product


class TestProductViews(TestCase):
    def setUp(self):
        Category.objects.create(
            name='test-category', friendly_name='test category')

        Product.objects.create(
            name='Test Name',
            price='99.99',
            colour='Test Colour',
            code='123456',
            description='Test Description',
        )

        User.objects.create_user(
            username='test_user', password='test_password')

        User.objects.create_superuser(
            username='test_super_user', password='test_password')

    def tearDown(self):
        Product.objects.all().delete()

    def test_get_all_products(self):
        """
        This test tests get all products
        """
        response = self.client.get('/products/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')

    def test_search_all_products_no_query_string(self):
        response = self.client.get('/products/', {'q': ''})
        self.assertRedirects(response, '/products/')

    def test_search_all_products_category_string(self):
        response = self.client.get('/products/', {'category': 'rugby_boots'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')

    def test_sort(self):
        response = self.client.get('/products/', {'sort': 'name'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')
        response = self.client.get('/products/', {'sort': 'category'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')
        response = self.client.get('/products/', {'sort': 'category', 'direction': 'desc'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')

    def test_get_product_detail(self):
        """
        This test tests get product details
        """
        product = Product.objects.get()
        response = self.client.get(f'/products/{product.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/product_detail.html')

    def test_add_product_as_superuser(self):
        """
        This test tests add product page as a superuser
        """
        self.client.login(username='test_super_user', password='test_password')
        response = self.client.get('/products/add/')
        self.assertTemplateUsed(response, 'products/add_product.html')

    def test_add_product_as_non_superuser(self):
        """
        This test tests add product page as a non superuser
        """
        self.client.login(username='test_user', password='test_password')
        response = self.client.get('/products/add/')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]), "Sorry, only store owners can do that.")

    def test_add_product_as_superuser_post(self):
        self.client.login(username='test_super_user', password='test_password')
        response = self.client.post('/products/add/', {
            'name': 'Test Name 2',
            'price': '99.99',
            'colour': 'Test Colour',
            'code': '12345678',
            'description': 'Test Description',
        })
        self.assertRedirects(response, '/products/2/')

    def test_get_edit_product_page(self):
        self.client.login(username='test_super_user', password='test_password')
        product = Product.objects.get()
        response = self.client.get(f'/products/edit/{product.id}/')
        self.assertTemplateUsed(response, 'products/edit_product.html')

    def test_edit_product_page_as_superuser(self):
        self.client.login(username='test_super_user', password='test_password')
        product = Product.objects.get()
        self.client.post(f'/products/edit/{product.id}/', {
            'name': 'Test Name Update',
            'price': '99.99',
            'colour': 'Test Colour Update',
            'code': '123456',
            'description': 'Test Description Update',
        })
        updated_product = Product.objects.get()
        self.assertEqual(updated_product.name, 'Test Name Update')
        self.assertEqual(updated_product.description, 'Test Description Update')

    def test_edit_product_page_as_non_superuser(self):
        self.client.login(username='test_user', password='test_password')
        product = Product.objects.get()
        response = self.client.post(f'/products/edit/{product.id}/', {
            'name': 'Test Name Update',
            'price': '99.99',
            'colour': 'Test Colour Update',
            'code': '123456',
            'description': 'Test Description Update',
        })
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]), "Sorry, only store owners can do that.")

    def test_delete_product_as_superuser(self):
        self.client.login(username='test_super_user', password='test_password')
        product = Product.objects.get()
        response = self.client.post(f'/products/delete/{product.id}/')
        self.assertRedirects(response, '/products/')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]), "Product deleted!")
        deleted_product = Product.objects.filter(id=product.id)
        self.assertEqual(len(deleted_product), 0)

    def test_delete_product_as_non_superuser(self):
        self.client.login(username='test_user', password='test_password')
        product = Product.objects.get()
        response = self.client.post(f'/products/delete/{product.id}/')
        self.assertRedirects(response, '/')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]), "Sorry, only store owners can do that.")
