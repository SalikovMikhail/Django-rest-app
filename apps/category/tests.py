import json
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Category
from django.urls import reverse
from .serializers import ListCategorySerializers


class CategoryTests(APITestCase):

    def setUp(self):
        self.category_django = Category.objects.create(title='django')

        self.valid_create_data = {
            'title': 'Roman',
            'books': []
        }

        self.invalid_data = {
            'title': '',
            'books': []
        }

        self.valid_put_data = {
            'title': 'Roman2',
            'books': []
        }

    def test_get_category_list(self):
        response = self.client.get(reverse('categories'))
        categories = Category.objects.all()
        serializer = ListCategorySerializers(categories, many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_get_category_single(self):
        response = self.client.get(reverse('category', kwargs={'pk': self.category_django.pk}))
        category = Category.objects.get(pk=self.category_django.pk)
        serializer = ListCategorySerializers(category)

        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single(self):
        response = self.client.get(reverse('category', kwargs={'pk': 10}))

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_post_create_valid_category(self):
        response = self.client.post(
            reverse('categories'),
            data=json.dumps(self.valid_create_data),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_post_create_invalid_category(self):
        response = self.client.post(
            reverse('categories'),
            data=json.dumps(self.invalid_data),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_put_valid_category(self):
        response = self.client.put(
            reverse('category', kwargs={'pk': self.category_django.pk}),
            data=json.dumps(self.valid_put_data),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_put_invalid_category(self):
        response = self.client.put(
            reverse('category', kwargs={'pk': self.category_django.pk}),
            data=json.dumps(self.invalid_data),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_delete_valid_category(self):
        response = self.client.delete(
            reverse('category', kwargs={"pk": self.category_django.pk})
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_invalid_category(self):
        response = self.client.delete(
            reverse('category', kwargs={"pk": 10})
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
