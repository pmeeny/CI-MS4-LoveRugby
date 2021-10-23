from django.test import TestCase

class TestBagViews(TestCase):

    def test_get_cart_page(self):
        """
        This test checks that the bag(cart) page
        is displayed
        """
        response = self.client.get('/bag/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bag/bag.html')