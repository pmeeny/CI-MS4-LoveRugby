# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.contrib.auth.models import User
from django.test import TestCase

# Internal:
from news.models import News, Comment

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class TestNewsModels(TestCase):
    """
    A class for testing news models
    """
    def setUp(self):
        """
        Create test user, news story and comment
        """
        test_user = User.objects.create_user(
            username='test_user', password='test_password')

        test_news_story = News.objects.create(
            title='Test Title',
            user=test_user,
            news_item_text='Test Item Text',
            image='TestImage.png',
            update_date='01/01/2021',
            create_date='01/01/2021',
            status=1,
        )

        Comment.objects.create(
            user=test_user,
            new_story=test_news_story,
            comment_text='Test Item Text',
            create_date='01/01/2021',
        )

    def tearDown(self):
        """
        Delete test user, news story and comment
        """
        User.objects.all().delete()
        News.objects.all().delete()
        Comment.objects.all().delete()

    def test_news_str_method(self):
        """
        This test tests the news str method and verifies
        """
        news_item = News.objects.get(title='Test Title')
        self.assertEqual((news_item.__str__()), news_item.title)

    def test_comment_str_method(self):
        """
        This test tests the news str method and verifies
        """
        comment = Comment.objects.get(comment_text='Test Item Text')
        self.assertEqual((comment.__str__()), comment.comment_text)
