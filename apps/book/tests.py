import json

from django.shortcuts import get_object_or_404
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase

from apps.user.models import User
from apps.category.models import Category
from apps.author.models import Author
from .models import Book

from .serializers import BookSerializer


class BookTests(APITestCase):

    def setUp(self):
        self.author_django = Author.objects.create(first_name='Sava', last_name='Savin', birth_date='1999-05-05')
        self.user_django = User.objects.create(first_name='Sava', last_name='Savin', email='mishasal@mail.ru', age=20)
        self.category_django = Category.objects.create(title='django')
        self.book_django = Book.objects.create(title='Book 1',
                                               description='Book 1 Hey!',
                                               release_date='1985-01-01',
                                               lessee=get_object_or_404(User, id=self.user_django.pk),
                                               category=get_object_or_404(Category, id=self.category_django.pk),
                                               author=get_object_or_404(Author, id=self.author_django.pk))

        self.valid_create_data = {
            'title': 'Roman1',
            'description': 'Book roman',
            'release_date': '1990-02-02',
            'lessee': 1,
            'category': 1,
            'author': 1
        }

        self.invalid_data = {
            'title': '',
            'description': 'Book roman',
            'release_date': '1990-02-02',
            'lessee': 1,
            'category': 1,
            'author': 1
        }

        self.valid_put_data = {
            'title': 'Roman2 two',
            'description': 'Book roman',
            'release_date': '1990-02-02',
            'lessee': 1,
            'category': 1,
            'author': 1
        }

    def test_get_book_list(self):
        response = self.client.get(reverse('books'))
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_get_book_single(self):
        response = self.client.get(reverse('book', kwargs={'pk': self.book_django.pk}))
        book = Book.objects.get(pk=self.book_django.pk)
        serializer = BookSerializer(book)

        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single(self):
        response = self.client.get(reverse('book', kwargs={'pk': 10}))

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_post_create_valid_book(self):
        response = self.client.post(
            reverse('book_create'),
            data=json.dumps(self.valid_create_data),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_post_create_invalid_book(self):
        response = self.client.post(
            reverse('book_create'),
            data=json.dumps(self.invalid_data),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_put_valid_book(self):
        response = self.client.put(
            reverse('book_update', kwargs={'pk': self.book_django.pk}),
            data=json.dumps(self.valid_put_data),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_put_invalid_book(self):
        response = self.client.put(
            reverse('book_update', kwargs={'pk': self.book_django.pk}),
            data=json.dumps(self.invalid_data),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_delete_valid_book(self):
        response = self.client.delete(
            reverse('book', kwargs={"pk": self.book_django.pk})
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_invalid_book(self):
        response = self.client.delete(
            reverse('book', kwargs={"pk": 10})
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
