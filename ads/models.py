from django.conf import settings
from django.db import models
from django.utils import timezone

from users.models import User

# Create your models here.
NULLABLE = {"blank": True, "null": True}


class Ad(models.Model):
    """Класс модели объявления"""
    title = models.CharField(max_length=100, verbose_name='Название товара')
    price = models.PositiveIntegerField(verbose_name='Цена товара')
    descriptions = models.CharField(max_length=500, verbose_name='Описание товара')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    image = models.ImageField(upload_to='notices/', verbose_name='Изображение товара', **NULLABLE)
    created_at = models.DateTimeField(default=timezone.now, verbose_name='Дата создания объявления')

    def __str__(self):
        return f'{self.title}-{self.price}'

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"
        ordering = ['-created_at']


class Comment(models.Model):
    """Класс модели отзывов"""
    text = models.CharField(max_length=100, verbose_name='Текст')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE, verbose_name='Объявление')
    created_at = models.DateTimeField(default=timezone.now, verbose_name='Время')

    def __str__(self):
        return f'{self.text}-{self.author}'

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        ordering = ['-created_at']
