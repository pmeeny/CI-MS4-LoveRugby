# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.contrib.auth.models import User
from django.contrib.messages import get_messages
from django.test import TestCase

# Internal:
from products.models import Category, Product, Review
from products.views import get_average_rating
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


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
        User.objects.all().delete()
        Review.objects.all().delete()

    def test_get_all_products(self):
        """
        This test tests get all products
        """
        response = self.client.get('/products/', {'search_term': 'test',
                                                  'current_categories': 'test'})
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
        response = self.client.get('/products/', {'sort': 'category',
                                                  'direction': 'desc'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')

    def test_get_product_detail(self):
        """
        This test tests get product details
        """
        product = Product.objects.get()
        response = self.client.get(f'/products/{product.id}/',
                                   {'product': product,
                                    'is_product_in_favourites': 'true'})
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
        self.assertEqual(str(messages[0]),
                         "Sorry, only store owners can do that.")

    def test_add_product_as_superuser_post(self):
        """
        This test tests add product page as a superuser
        """
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
        """
        This test tests edit product page(get) as a superuser
        """
        self.client.login(username='test_super_user', password='test_password')
        product = Product.objects.get()
        response = self.client.get(f'/products/edit/{product.id}/')
        self.assertTemplateUsed(response, 'products/edit_product.html')

    def test_edit_product_page_as_superuser(self):
        """
        This test tests edit product page(post) as a superuser
        """
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
        """
        This test tests edit product page as a non superuser
        """
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
        self.assertEqual(str(messages[0]), "Sorry, "
                                           "only store owners can do that.")

    def test_delete_product_as_superuser(self):
        """
        This test tests delete product as a superuser
        """
        self.client.login(username='test_super_user', password='test_password')
        product = Product.objects.get()
        response = self.client.post(f'/products/delete/{product.id}/')
        self.assertRedirects(response, '/products/')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]), "Product deleted!")
        deleted_product = Product.objects.filter(id=product.id)
        self.assertEqual(len(deleted_product), 0)

    def test_delete_product_as_non_superuser(self):
        """
        This test tests delete product as a non superuser
        """
        self.client.login(username='test_user', password='test_password')
        product = Product.objects.get()
        response = self.client.post(f'/products/delete/{product.id}/')
        self.assertRedirects(response, '/')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]), "Sorry, "
                                           "only store owners can do that.")

    def test_add_review_to_product_failure(self):
        """
        This test tests add review to product as a failed case
        """
        self.client.login(username='test_user', password='test_password')
        product = Product.objects.get()
        response = self.client.post(f'/products/add_review/{product.id}/')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]), "Failed to add product review")

    def test_add_review_to_product(self):
        """
        This test tests add review to product as a success case
        """
        test_user = User.objects.create_user(
            username='test_user1', password='test_password')
        self.client.login(username='test_user', password='test_password')
        product = Product.objects.get()

        Review.objects.create(
            user=test_user,
            product=product,
            product_rating='5',
            review_text='Test Review Text',
        )
        response = self.client.post(f'/products/add_review/{product.id}/',
                                    {'product_rating': '5',
                                     'review_text': 'Test Review Text'})
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]), "Successfully added a review!")

    def test_add_two_review_one_user_to_product(self):
        """
        This test tests add two reviews to a product, failure case
        """
        test_user2 = User.objects.create_user(
            username='test_user2', password='test_password')
        self.client.login(username='test_user', password='test_password')
        product = Product.objects.get()

        Review.objects.create(
            user=test_user2,
            product=product,
            product_rating='5',
            review_text='Test Review Text',
        )
        self.client.post(f'/products/add_review/{product.id}/',
                         {'product_rating': '4',
                          'review_text': 'Test Review Text1'})
        response = self.client.post(f'/products/add_review/{product.id}/',
                                    {'product_rating': '3',
                                     'review_text': 'Test Review Text2'})
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]), "Successfully added a review!")
        self.assertEqual(str(messages[1]), "You have already reviewed "
                                           "this product!")

    def test_delete_review_from_product(self):
        """
        This test tests delete review from a product
        """
        test_user2 = User.objects.create_user(
            username='test_user4', password='test_password')
        self.client.login(username='test_user4', password='test_password')
        product = Product.objects.get()

        Review.objects.create(
            user=test_user2,
            product=product,
            product_rating='5',
            review_text='Test Review Text',
        )
        # self.client.post(f'/products/add_review/{product.id}/',
        #                  {'product_rating': '4',
        #                  'review_text': 'Test Review Text'})
        response = self.client.post(
            f'/products/delete_review/{product.id}/{test_user2.username}/')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]), "Your review was deleted")

    def test_delete_review_from_product_no_permission(self):
        """
        This test tests delete review from a product
        """
        test_user2 = User.objects.create_user(
            username='test_user2', password='test_password')
        self.client.login(username='test_user', password='test_password')
        product = Product.objects.get()

        Review.objects.create(
            user=test_user2,
            product=product,
            product_rating='5',
            review_text='Test Review Text',
        )
        self.client.post(f'/products/add_review/{product.id}/',
                         {'product_rating': '4',
                          'review_text': 'Test Review Text1'})
        response = self.client.post(
            f'/products/delete_review/{product.id}/{test_user2.username}/')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]), "Successfully added a review!")
        self.assertEqual(str(messages[1]), "Sorry, you don't have permission "
                                           "to do that.")

    def test_get_average_rating_two_reviews(self):
        """
        This test tests delete review from a product
        """
        product = Product.objects.get()
        test_user3 = User.objects.create_user(
            username='test_user3', password='test_password')
        self.client.login(username='test_user3', password='test_password')
        review1 = Review.objects.create(
            user=test_user3,
            product=product,
            product_rating='5',
            review_text='Test Review Text',
        )
        test_user4 = User.objects.create_user(
            username='test_user4', password='test_password')
        self.client.login(username='test_user4', password='test_password')
        review2 = Review.objects.create(
            user=test_user4,
            product=product,
            product_rating='4',
            review_text='Test Review Text 2',
        )
        reviews = Review.objects.filter(product=product)
        average_rating = get_average_rating(reviews)
        self.assertEqual(average_rating, 4.5)

    def test_get_average_rating_no_reviews(self):
        """
        This test tests delete review from a product
        """
        product = Product.objects.get()
        reviews = Review.objects.filter(product=product)
        average_rating = get_average_rating(reviews)
        self.assertEqual(average_rating, 0)

    def test_sale_item(self):
        """
        This test tests the sale item view
        """
        response = self.client.get('/products/sale_items')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/sale_items.html')
