from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient, APITestCase, APISimpleTestCase, APIRequestFactory
from .models import TODOUser
from .views import TODOUserViewSet
from mixer.backend.django import mixer


class UserTestCase(TestCase):
    def test_user_list(self):
        client = APIClient()
        res = client.get('/api/tdusers/')
        self.assertEqual(res.status_code, status.HTTP_200_OK)


class UserApiTestCase(APITestCase):
    def setUp(self):
        TODOUser.objects.create_superuser('Qwerty', 'a@gmail.com', 'qwertyadm')

    def test_todousers_list(self):
        user=mixer.blend(TODOUser)
        self.client.login(username='Qwerty', password='qwertyadm')
        res = self.client.get('/api/tdusers/')
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data), 2)

    def test_factory(self):
        factory = APIRequestFactory()
        view = TODOUserViewSet.as_view({'get': 'list'})
        request = factory.get('/api/tdusers/')
        res = view(request)
        self.assertEqual(res.status_code, status.HTTP_200_OK)


class FuncTest(APISimpleTestCase):
    def testFunc(self):
        self.assertEqual(True, True)


class MixerUserApiTestCase(APITestCase):
    def test_todousers_list(self):
        todouser = mixer.blend(TODOUser)
