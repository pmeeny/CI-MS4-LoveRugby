# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.contrib.auth.models import User
from django.test import TestCase

# Internal:
from products.models import Category, Product, Review
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class TestProductModels(TestCase):
    """
    A class for testing product models
    """
    def setUp(self):
        """
        Create test user, category, product and review
        """
        test_user = User.objects.create_user(
            username='test_user', password='test_password')

        Category.objects.create(
            name='test-category', friendly_name='test category')

        product = Product.objects.create(
            name='Test Name',
            price='99.99',
            colour='Test Colour',
            code='123456',
            description='Test Description',
        )
        Review.objects.create(
            user=test_user,
            product=product,
            product_rating='5',
            review_text='Test Review Text',
        )
        
    def tearDown(self):
        """
        Delete test user, category, product and review
        """
        User.objects.all().delete()
        Category.objects.all().delete()
        Product.objects.all().delete()
        Review.objects.all().delete()

    def test_category_str_method(self):
        """
        This test tests the categories str method and verifies
        """
        category = Category.objects.get(name='test-category')
        self.assertEqual((category.__str__()), category.name)
        self.assertEqual(category.get_friendly_name(), category.friendly_name)

    def test_product_str_method(self):
        """
        This test tests the products str method and verifies
        """
        product = Product.objects.get(code='123456')
        self.assertEqual((product.__str__()), product.name)

    def test_review_str_method(self):
        """
        This test tests the reviews str method and verifies
        """
        review = Review.objects.get(review_text='Test Review Text')
        self.assertEqual((review.__str__()), review.review_text)
