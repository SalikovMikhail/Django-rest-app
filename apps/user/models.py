from django.db import models


class User(models.Model):
    """Пользователи"""
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    email = models.EmailField(unique=True)
    age = models.IntegerField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
