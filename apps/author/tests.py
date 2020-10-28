import json
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Author
from django.urls import reverse
from .serializers import ListAuthorSerializers


class AuthorTests(APITestCase):

    def setUp(self):
        self.author_django = Author.objects.create(first_name='Sava', last_name='Savin', birth_date='1999-05-05')

        self.valid_create_data = {
            'first_name': 'Roman',
            'last_name': 'Bora',
            'birth_date': '1991-02-02',
            'books': []
        }

        self.invalid_data = {
            'first_name': '',
            'last_name': 'Bora',
            'birth_date': '1991-02-02',
            'books': []
        }

        self.valid_put_data = {
            'first_name': 'Roman2',
            'last_name': 'Bora2',
            'birth_date': '1991-02-02',
            'books': []
        }

    def test_get_author_list(self):
        response = self.client.get(reverse('authors'))
        authors = Author.objects.all()
        serializer = ListAuthorSerializers(authors, many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_get_author_single(self):
        response = self.client.get(reverse('author_detail', kwargs={'pk': self.author_django.pk}))
        author = Author.objects.get(pk=self.author_django.pk)
        serializer = ListAuthorSerializers(author)

        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single(self):
        response = self.client.get(reverse('author_detail', kwargs={'pk': 10}))

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_post_create_valid_author(self):
        response = self.client.post(
            reverse('authors'),
            data=json.dumps(self.valid_create_data),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_post_create_invalid_author(self):
        response = self.client.post(
            reverse('authors'),
            data=json.dumps(self.invalid_data),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_put_valid_author(self):
        response = self.client.put(
            reverse('author_detail', kwargs={'pk': self.author_django.pk}),
            data=json.dumps(self.valid_put_data),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_put_invalid_author(self):
        response = self.client.put(
            reverse('author_detail', kwargs={'pk': self.author_django.pk}),
            data=json.dumps(self.invalid_data),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_delete_valid_author(self):
        response = self.client.delete(
            reverse('author_detail', kwargs={"pk": self.author_django.pk})
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_invalid_author(self):
        response = self.client.delete(
            reverse('author_detail', kwargs={"pk": 10})
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
