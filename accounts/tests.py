from django.test import TestCase
from .models import User

#making sure User class does create a user.
class UserManagerTestCase(TestCase):
    def test_main_create_user(self):
        user = User.objects.create_user('bart@gmail.com', 'password123')
        self.assertTrue(isinstance(user, User))
