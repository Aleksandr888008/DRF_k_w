from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    username = None

    email = models.EmailField(verbose_name='email', unique=True)
    phone = models.CharField(max_length=50, verbose_name='телефон', **NULLABLE)
    chat_id = models.CharField(max_length=100, verbose_name='Ник пользователя в телеграмм')

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = []
