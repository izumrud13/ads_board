from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
NULLABLE = {"blank": True, "null": True}


class UserRoles:
    USER = 'user'
    ADMIN = 'admin'

    choices = ((USER, 'Пользователь'),
               (ADMIN, 'Администратор'),)


class User(AbstractUser):
    """Класс модели пользователя"""
    email = models.EmailField(unique=True, verbose_name='Почта')
    first_name = models.CharField(max_length=100, verbose_name='Имя')
    last_name = models.CharField(max_length=100, verbose_name='Фамилия')
    phone = models.CharField(max_length=50, verbose_name='Телефон')
    image = models.ImageField(upload_to='users/', verbose_name='Аватар', **NULLABLE)
    role = models.CharField(max_length=5, choices=UserRoles.choices, default=UserRoles.USER, verbose_name='Роль')
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
