from django.db import models


class Author(models.Model):
    """Авторы книг"""
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    birth_date = models.DateField(blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
