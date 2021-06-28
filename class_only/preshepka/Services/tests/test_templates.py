from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse
from Services.models import Service


class ServiceTemplateTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = get_user_model().objects.create_user(
            username='test_user',
            email='test@mail.com',
            password='test_password'
        )
        self.service = Service.objects.create(
            title='test_service',
            descriptions='test_description',
            price='1',
            user=self.user
        )

    def test_home_template(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'service/all_services.html')

    def test_detail_service_template(self):
        self.client.login(
            username='test_user',
            password='test_password'
        )
        response = self.client.get(reverse('detail', args='1'))
        self.assertTemplateUsed(response, 'service/service_id.html')

    def test_update_service_template(self):
        response = self.client.get(reverse('update', args='1'))
        self.assertTemplateUsed(response, 'service/update_service.html')

    def test_delete_service_template(self):
        response = self.client.get(reverse('delete', args='1'))
        self.assertTemplateUsed(response, 'service/delete_service.html')

    def test_create_service_template(self):
        response = self.client.get(reverse('add_service'))
        self.assertTemplateUsed(response, 'service/add_service.html')

    def test_service_search_template(self):
        response = self.client.get('/search_result/', {
            'user_search': 'test'
        })
        self.assertTemplateUsed(response, 'service/search_list.html')