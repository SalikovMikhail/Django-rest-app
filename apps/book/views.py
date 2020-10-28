from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.generics import get_object_or_404
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView

from .serializers import BookSerializer, BookCreateSerializer
from .models import Book
from apps.author.models import Author
from apps.category.models import Category
from apps.user.models import User


class BookView(ListAPIView):
    """Отдает список книг"""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['title', 'description']


class BookDetailView(RetrieveDestroyAPIView):
    """Отдает или удалаяет книгу по id"""
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookCreateView(CreateAPIView):
    """Создает книгу в БД, привязывает к ней автора, категории и "арендующего" человека"""
    queryset = Book.objects.all()
    serializer_class = BookCreateSerializer

    def perform_create(self, serializer):
        author = get_object_or_404(Author, id=self.request.data.get('author'))
        user = get_object_or_404(User, id=self.request.data.get('lessee'))
        category = get_object_or_404(Category, id=self.request.data.get('category'))
        return serializer.save()


class BookUpdateView(RetrieveUpdateAPIView):
    """Отдает или обновляет книгу, используя id"""
    queryset = Book.objects.all()
    serializer_class = BookCreateSerializer
