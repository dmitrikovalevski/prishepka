from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from users.views import update_user_account
from users.models import UserInfo
from users.forms import UserAccountUpdateForm, UpdateUserForm
from django.db.models import signals
from users.signals import create_userinfo


class UserTemplatesTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create(
            username='test_user',
            password='test_password',
            email='test@mail.com'
        )

    def test_login_template(self):
        response = self.client.get(reverse('login'))
        self.assertTemplateUsed(response, 'registration/login.html')

    def test_create_user_template(self):
        response = self.client.get(reverse('add_user'))
        self.assertTemplateUsed(response, 'users/add.html')

    def test_account_user_template(self):
        response = self.client.get(reverse('account', args='1'))
        self.assertTemplateUsed(response, 'users/account_detail.html')

    def test_password_reset_templates(self):
        response = self.client.get(reverse('forgot'))
        self.assertTemplateUsed(response, 'registration/reset_form.html')

    def test_password_reset_done_templates(self):
        response = self.client.get(reverse('password_reset_done'))
        self.assertTemplateUsed(response, 'registration/reset_done.html')

    def test_password_reset_confirm_templates(self):
        uidb64 = None
        token = None
        response = self.client.get(reverse('password_reset_confirm', kwargs={
            'uidb64': uidb64,
            'token': token
        }))
        self.assertTemplateUsed(response, 'registration/reset_confirm.html')

    def test_password_reset_complete_templates(self):
        response = self.client.get(reverse('password_reset_complete'))
        self.assertTemplateUsed(response, 'registration/reset_complete.html')
