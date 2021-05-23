from django.test import Client, TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from .models import Service


class SimpleTests(TestCase):

    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_about_page_status_code(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)

