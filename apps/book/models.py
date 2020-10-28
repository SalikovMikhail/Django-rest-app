from django.db import models

from apps.user.models import User
from apps.category.models import Category
from apps.author.models import Author


class Book(models.Model):
    """Книги"""
    title = models.CharField(max_length=70, db_index=True)
    description = models.TextField(blank=True)
    release_date = models.DateField(blank=True)
    lessee = models.ForeignKey(User, on_delete=models.PROTECT, related_name='books', blank=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='books', blank=True)
    author = models.ForeignKey(Author, on_delete=models.PROTECT, related_name='books', blank=True)

    def __str__(self):
        return f'{self.title}, написал: {self.author}'


