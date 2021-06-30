from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse


class UserModelTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create(
            username='test_user',
            password='test_password',
            email='test@mail.com'
        )
        # При создании пользваталется в setUp() с помощью сигнала
        # self.user привязывается к UserInfo()

    def test_add_user_to_userinfo(self):
        self.assertEqual(self.user.username, self.user.userinfo.user.username)

    def test_check_user_fields(self):
        self.assertEqual(self.user.username, 'test_user')
        self.assertEqual(self.user.password, 'test_password')
        self.assertEqual(self.user.email, 'test@mail.com')

    def test_create_user(self):
        response = self.client.post(reverse('add_user'), {
            'username': 'new_user',
            'email': 'new_user@mail.com',
            'password1': 'qwerty',
            'password2': 'qwerty'
        }, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'new_user')
        self.assertContains(response, 'new_user@mail.com')







