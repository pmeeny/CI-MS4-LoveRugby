from django.contrib.auth.models import User
from django.test import TestCase

from products.models import Category, Product, Review


class TestProductModels(TestCase):
    def setUp(self):
        test_user = User.objects.create_user(
            username='test_user', password='test_password')

        Category.objects.create(
            name='test-category', friendly_name='test category')

        Product.objects.create(
            name='Test Name',
            price='99.99',
            colour='Test Colour',
            code='123456',
            description='Test Description',
        )
        Review.objects.create(
            user= test_user,
            product='Test Product',
            product_rating='5',
            review_text='Test Review Text',
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
        product = Product.objects.get(code='Test Review Text')
        self.assertEqual((product.__str__()), product.name)

    def test_review_str_method(self):
        """
        This test tests the reviews str method
        """
        review = Review.objects.get(review_text='Test Review Text')
        self.assertEqual((review.__str__()), review.review_text)