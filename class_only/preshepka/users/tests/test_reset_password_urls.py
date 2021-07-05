from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse


class UserResetPasswordUrlTest(TestCase):
    '''
    Все тесты проверяют правильно ли указаны пути для смены пароля
    '''

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create(
            username='test_user',
            password='test_password',
            email='test@mail.com'
        )

    def test_password_reset_url(self):
        response = self.client.get(reverse('forgot'))
        self.assertEqual(response.status_code, 200)

    def test_password_reset_done_url(self):
        response = self.client.get(reverse('password_reset_done'))
        self.assertEqual(response.status_code, 200)

    def test_password_reset_confirm_url(self):
        uidb64 = None
        token = None
        response = self.client.get(reverse('password_reset_confirm', kwargs={
            'uidb64': uidb64,
            'token': token
        }))
        self.assertEqual(response.status_code, 200)

    def test_password_reset_complete_url(self):
        response = self.client.get(reverse('password_reset_complete'))
        self.assertEqual(response.status_code, 200)
