from django.test import TestCase

# Create your tests here.

from django.contrib.auth import get_user_model
from django.urls import reverse

from .models import CustomUser

class Userests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username = 'doaa',
            email = 'doaa@gmail.com',
            password = 'doaa1996'
        )

    def test__status(self):
        try:
            self.user2 = get_user_model().objects.create_user(
                        username = 'doaa',
                        email = 'doaa@gmail.com',
                        password = 'doaa1996'
                    )
        except:
            self.user2 = None

        self.assertEqual(self.user2,None)

    def test_login(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code , 200)