from django.test import TestCase
from mixer.backend.django import mixer
from .models import TODO, UsersProject, TODOUser
from rest_framework import status
from rest_framework.test import APIClient, APITestCase, APISimpleTestCase, APIRequestFactory


class UsersProjApiTestCase(APITestCase):
    def test_project_list(self):
        project = mixer.blend(UsersProject)
        res = self.client.get('/api/projects/')
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        print(res.data)
        self.assertEqual(len(res.data), 4)
