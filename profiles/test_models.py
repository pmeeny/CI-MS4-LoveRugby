from django.test import TestCase

from django.contrib.auth.models import User
from profiles.models import UserProfile

class TestProfileModels(TestCase):

    def setUp(self):
        testuser = User.objects.create_user(
            username='testuser',
            password='testpassword',
            email='testuser@email.com')
        testuser.save()

    def test_profile_string_method(self):
        testuser = User.objects.get(username='testuser')
        profile = UserProfile.objects.get(user=testuser)
        self.assertEqual(str(profile), profile.user.username)