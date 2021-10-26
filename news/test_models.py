from django.contrib.auth.models import User
from django.test import TestCase

from news.models import News, Comment


class TestNewsModels(TestCase):
    def setUp(self):

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

    def test_news_str_method(self):
        """
        This test tests the news str method
        """
        news_item = News.objects.get(title='Test Title')
        self.assertEqual((news_item.__str__()), news_item.title)

    def test_comment_str_method(self):
        """
        This test tests the news str method
        """
        comment = Comment.objects.get(comment_text='Test Item Text')
        self.assertEqual((comment.__str__()), comment.comment_text)
