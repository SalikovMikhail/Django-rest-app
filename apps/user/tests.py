import json
from rest_framework import status
from rest_framework.test import APITestCase

from .models import User
from django.urls import reverse
from .serializers import UserListSerializer


class UserTests(APITestCase):

    def setUp(self):
        self.user_django = User.objects.create(first_name='Sava', last_name='Savin', email='mishasal@mail.ru', age=20)

        self.valid_create_data = {
            'first_name': 'Roman',
            'last_name': 'Bora',
            'email': 'boran@mail.ru',
            'age': 23,
            'books': []
        }

        self.invalid_data = {
            'first_name': '',
            'last_name': 'Bora',
            'email': 'boran@mail.ru',
            'age': 23,
            'books': []
        }

        self.valid_put_data = {
            'first_name': 'Roman2',
            'last_name': 'Bora2',
            'email': 'boran@mail.ru',
            'age': 23,
            'books': []
        }

    def test_get_user_list(self):
        response = self.client.get(reverse('users'))
        users = User.objects.all()
        serializer = UserListSerializer(users, many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_get_user_single(self):
        response = self.client.get(reverse('user', kwargs={'pk': self.user_django.pk}))
        user = User.objects.get(pk=self.user_django.pk)
        serializer = UserListSerializer(user)

        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single(self):
        response = self.client.get(reverse('user', kwargs={'pk': 10}))

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_post_create_valid_user(self):
        response = self.client.post(
            reverse('users'),
            data=json.dumps(self.valid_create_data),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_post_create_invalid_user(self):
        response = self.client.post(
            reverse('users'),
            data=json.dumps(self.invalid_data),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_put_valid_user(self):
        response = self.client.put(
            reverse('user', kwargs={'pk': self.user_django.pk}),
            data=json.dumps(self.valid_put_data),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_put_invalid_user(self):
        response = self.client.put(
            reverse('user', kwargs={'pk': self.user_django.pk}),
            data=json.dumps(self.invalid_data),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_delete_valid_user(self):
        response = self.client.delete(
            reverse('user', kwargs={"pk": self.user_django.pk})
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_invalid_user(self):
        response = self.client.delete(
            reverse('user', kwargs={"pk": 10})
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
