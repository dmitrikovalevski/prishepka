from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse


class UserUrlTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='test_user',
            password='test_password',
            email='test@mail.com',
        )

    def test_login_url(self):
        response = self.client.get(reverse('login'), follow=True)
        self.assertEqual(response.status_code, 200)

    def test_logout_url(self):
        response = self.client.get(reverse('logout'), follow=True)
        self.assertEqual(response.status_code, 200)

    def test_create_user_url(self):
        response = self.client.get(reverse('add_user'), follow=True)
        self.assertEqual(response.status_code, 200)

    def test_account_user_url(self):
        self.client.login(
            username='test_user',
            password='test_password',
        )
        response = self.client.get(reverse('account', args='1'))
        self.assertEqual(response.status_code, 200)

    def test_update_user_url(self):
        self.client.login(
            username='test_user',
            password='test_password'
        )
        response = self.client.get(reverse('account_update'))
        self.assertEqual(response.status_code, 200)
