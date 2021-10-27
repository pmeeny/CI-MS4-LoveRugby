from django.contrib.auth.models import User
from django.contrib.messages import get_messages
from django.test import TestCase

from news.models import News


class TestNewsItemViews(TestCase):
    def setUp(self):
        test_user = User.objects.create_user(
            username='test_user', password='test_password')

        test_super_user = User.objects.create_superuser(
            username='test_super_user', password='test_password')

        News.objects.create(
            title='Test Title',
            user=test_user,
            news_item_text='Test Item Text',
            image='TestImage.png',
            update_date='01/01/2021',
            create_date='01/01/2021',
            status=1,
        )

        News.objects.create(
            title='Test Title 1',
            user=test_super_user,
            news_item_text='Test Item Text 1',
            image='TestImage1.png',
            update_date='01/01/2021',
            create_date='01/01/2021',
            status=1,
        )

    def tearDown(self):
        News.objects.all().delete()

    def test_get_all_news_items(self):
        """
        This test tests get all news items
        """
        response = self.client.get('/news/')
        self.assertEqual(News.objects.count(), 2)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'news/news.html')

    def test_manage_news_items(self):
        """
        This test tests manage news items
        """
        response = self.client.get('/news/manage_news_items/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'news/manage_news_items.html')

    def test_get_add_news_item_as_superuser(self):
        """
        This test tests get add news item as a superuser
        """
        self.client.login(username='test_super_user', password='test_password')
        response = self.client.get('/news/add_news_item/')
        self.assertTemplateUsed(response, 'news/add_news_item.html')

    def test_get_add_news_item_as_non_superuser(self):
        """
        This test tests get add news item as a non superuser
        """
        self.client.login(username='test_user', password='test_password')
        response = self.client.get('/news/add_news_item/')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]), "Sorry, only store owners can do that.")

    def test_add_news_item_as_superuser_post(self):
        """
        This test tests post add news item as a superuser
        """
        self.client.login(username='test_super_user', password='test_password')
        response = self.client.post('/news/add_news_item/', {
            'title': 'Test Title 2',
            'user': '{test_super_user}',
            'news_item_text': 'Test Item Text 1',
            'image': 'TestImage1.png',
            'update_date': '01/01/2021',
            'create_date': '01/01/2021',
            'status': '1',
        })
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]), "Your news item was posted successfully!")
        self.assertRedirects(response, '/news/')

    def test_add_news_item_as_superuser_post_already_exists(self):
        """
        This test tests post add news item as a superuser
        It is a negative test case and
        """
        self.client.login(username='test_super_user', password='test_password')
        self.client.post('/news/add_news_item/', {
            'title': 'Test Title 2',
            'user': '{test_super_user}',
            'news_item_text': 'Test Item Text 1',
            'image': 'TestImage1.png',
            'update_date': '01/01/2021',
            'create_date': '01/01/2021',
            'status': '1',
        })
        response = self.client.post('/news/add_news_item/', {
            'title': 'Test Title 2',
            'user': '{test_super_user}',
            'news_item_text': 'Test Item Text 1',
            'image': 'TestImage1.png',
            'update_date': '01/01/2021',
            'create_date': '01/01/2021',
            'status': '1',
        })
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[1]), "Your news item failed to add, Please try again")

    def test_get_edit_news_item_page(self):
        """
        This test tests the edit_news_item page
        """
        self.client.login(username='test_super_user', password='test_password')
        news_item = News.objects.get(title='Test Title')
        response = self.client.get(f'/news/edit_news_item/{news_item.id}/')
        self.assertTemplateUsed(response, 'news/edit_news_item.html')

    def test_edit_news_item_as_superuser_post(self):
        """
        This test tests post edit news item as a superuser
        """
        self.client.login(username='test_super_user', password='test_password')
        news_item = News.objects.get(title='Test Title')
        response = self.client.post(f'/news/edit_news_item/{news_item.id}/', {
            'title': 'Test Title 2',
            'user': '{test_super_user}',
            'news_item_text': 'Test Item Text 1',
            'image': 'TestImage1.png',
            'update_date': '01/01/2022',
            'create_date': '01/01/2022',
            'status': '1',
        })
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]), "Test Title 2 was successfully updated")
        self.assertRedirects(response, '/news/manage_news_items/')

    def test_get_edit_news_item_as_non_superuser(self):
        """
        This test tests get add news item as a non superuser
        """
        self.client.login(username='test_user', password='test_password')
        news_item = News.objects.get(title='Test Title')
        response = self.client.post(f'/news/edit_news_item/{news_item.id}/', {
            'title': 'Test Title 2',
            'user': '{test_super_user}',
            'news_item_text': 'Test Item Text 1',
            'image': 'TestImage1.png',
            'update_date': '01/01/2022',
            'create_date': '01/01/2022',
            'status': '1',
        })
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]), "Sorry, only store owners can do that.")

    def test_delete_news_item_as_non_superuser(self):
        """
        This test tests delete news item as a non superuser
        """
        self.client.login(username='test_user', password='test_password')
        news_item = News.objects.get(title='Test Title')
        response = self.client.post(f'/news/delete_news_item/{news_item.id}/', {
        })
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]), "Sorry, only store owners can do that.")

    def test_delete_news_item_as_superuser(self):
        """
        This test tests delete news item as a superuser
        """
        self.client.login(username='test_super_user', password='test_password')
        news_item = News.objects.get(title='Test Title')
        response = self.client.post(f'/news/delete_news_item/{news_item.id}/', {
        })
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]), "Test Title Successfully Deleted")
        self.assertEqual(News.objects.count(), 1)
        news_item = News.objects.get(title='Test Title 1')
        response = self.client.post(f'/news/delete_news_item/{news_item.id}/', {
        })
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]), "Test Title Successfully Deleted")
        self.assertEqual(News.objects.count(), 0)
