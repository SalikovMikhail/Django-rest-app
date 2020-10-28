from rest_framework import serializers
from .models import Book
from apps.author.models import Author
from apps.category.models import Category
from apps.user.models import User


class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = ('id', 'first_name', 'last_name')


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'title')


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name')


class BookSerializer(serializers.ModelSerializer):

    author = AuthorSerializer()
    lessee = UserSerializer()
    category = CategorySerializer()

    class Meta:
        model = Book
        fields = ('id', 'title', 'description', 'release_date', 'author', 'lessee', 'category')


class BookCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ('id', 'title', 'description', 'release_date', 'author', 'lessee', 'category')