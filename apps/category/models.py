from django.db import models


class Category(models.Model):
    """Жанры/категории книг"""
    title = models.CharField(max_length=25, db_index=True)

    def __str__(self):
        return f'{self.title}'
