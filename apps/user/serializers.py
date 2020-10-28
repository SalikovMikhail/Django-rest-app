from rest_framework import serializers

from .models import User
from apps.book.models import Book


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ('id', 'title')


class UserListSerializer(serializers.ModelSerializer):
    """Список пользователей"""

    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'age', 'books')
