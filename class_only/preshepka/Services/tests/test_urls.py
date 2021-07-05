from django.test import TestCase, Client
from Services.models import Service


class ServiceUrlTest(TestCase):
    '''
    Все тетсты проверят действуют ли указанные в тестах пути
    '''

    def setUp(self):
        self.client = Client()
        self.service = Service.objects.create(
            title='test_title',
            descriptions='test_description',
            price='100'
        )

    def test_home_url(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_service_detail_url(self):
        response = self.client.get('/detail/1')
        self.assertEqual(response.status_code, 301)

    def test_service_update_url(self):
        response = self.client.get('/detail/1/update/')
        self.assertEqual(response.status_code, 200)

    def test_service_delete_url(self):
        response = self.client.get('/detail/1/delete')
        self.assertEqual(response.status_code, 301)

    def test_service_create_url(self):
        response = self.client.get('/add_service/')
        self.assertEqual(response.status_code, 200)

    def test_service_search_url(self):
        response = self.client.get('/search_result/', {
            'user_search': 'test'
        })
        self.assertEqual(response.status_code, 200)
