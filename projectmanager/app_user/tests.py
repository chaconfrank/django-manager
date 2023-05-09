import json

import pytest
from rest_framework.test import APIClient
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status

from .models import User


@pytest.mark.django_db
class UserAPITestCase(APITestCase):

    def __int__(self):
        self.client = APIClient()

    def setUp(self):
        self.user1 = User.objects.create(email='user1@test.com', first_name='John', last_name='Doe')
        self.user2 = User.objects.create(email='user2@test.com', first_name='Jane', last_name='Doe')

    def test_list_users(self):
        url = reverse('app_user:users')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_create_user(self):
        url = reverse('app_user:users')
        data = {'email': 'user3@test.com', 'first_name': 'Sarah', 'last_name': 'Connor'}
        response = self.client.post(url, data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 3)