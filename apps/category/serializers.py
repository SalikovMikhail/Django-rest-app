from rest_framework import serializers

from .models import Category
from apps.book.models import Book


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ('id', 'title')


class ListCategorySerializers(serializers.ModelSerializer):
    """Список категорий/жанров"""

    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ('id', 'title', 'books')
