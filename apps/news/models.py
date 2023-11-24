from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class News(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Заголовок',
    )
    description = models.TextField(
        verbose_name='Описание',
    )
    date = models.DateField(
        auto_now_add=True,
        verbose_name='Дата',
    )
    image = models.ImageField(
        upload_to='news/',
        verbose_name='Изображение',
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор',
        related_name='news',
    )

    def __str__(self):
        return f'Новость {self.title} от автора: {self.author}'

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
