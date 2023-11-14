from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    username = models.CharField(unique=True, max_length=25, verbose_name='Имя пользователя', **NULLABLE)
    email = models.EmailField(verbose_name='Почта')
    telegram = models.CharField(max_length=50, verbose_name='Телеграмм', **NULLABLE)
    REQUIRED_FIELDS = ["email", "telegram"]
