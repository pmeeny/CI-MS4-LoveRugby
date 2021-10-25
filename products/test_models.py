from django.test import TestCase

from products.models import Category, Product


class TestProductModels(TestCase):
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

    def test_category_str_method(self):
        """
        This test tests the categories str method
        """
        category = Category.objects.get(name='test-category')
        self.assertEqual((category.__str__()), category.name)
        self.assertEqual(category.get_friendly_name(), category.friendly_name)

    def test_product_str_method(self):
        """
        This test tests the products str method
        """
        product = Product.objects.get(code='123456')
        self.assertEqual((product.__str__()), product.name)