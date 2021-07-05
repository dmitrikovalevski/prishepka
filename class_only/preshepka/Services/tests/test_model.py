from django.test import TestCase, Client
from django.contrib.auth.models import User
from Services.models import Service


class ServiceModelTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='test_user',
            password='test_password',
            email='test@mail.com'
        )
        self.service = Service.objects.create(
            title='test_title',
            descriptions='test_descriptions',
            price='100',
            user=self.user
        )

    # Если возьмёт вызовем объект он нам вернёт __str__метод
    def test_service_string_method(self):
        service = Service.objects.get(pk='1')
        self.assertEqual(service.title, 'test_title')

    # Проверим все ли поля модели заполнены
    def test_service_fields_content_exist(self):
        self.assertEqual(self.service.title, 'test_title')
        self.assertEqual(self.service.descriptions, 'test_descriptions')
        self.assertEqual(self.service.price, '100')
        self.assertEqual(self.service.user, self.user)

    # Если пользователь перейдёт по ссылке то увидит контент
    def test_service_content_is_exist_in_view(self):
        self.client.login(
            username='test_user',
            password='test_password'
        )
        response = self.client.get('/detail/1/')
        self.assertContains(response, 'test_title')
        self.assertContains(response, 'test_descriptions')
        self.assertContains(response, '100')
        self.assertContains(response, self.user)

    # Создадим новую услугу и перейдём по перенаправлению.
    # Проверим на наличие новго контента.
    def test_create_service(self):
        self.client.login(
            username='test_user',
            password='test_password'
        )
        response = self.client.post('/add_service/', {
            'title': 'create title',
            'descriptions': 'create description',
            'price': '500',
            'user': self.user
        }, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'create title')
        self.assertContains(response, 'create description')
        self.assertContains(response, '500')
        self.assertContains(response, self.user)

    # Проверим обновляется ли наша услуга
    def test_update_service(self):
        response = self.client.post('/detail/1/update', {
            'title': 'update new title',
            'descriptions': 'update new description',
            'price': '200',
            'user': self.user
        }, follow=True)
        self.assertEqual(response.status_code, 200)

