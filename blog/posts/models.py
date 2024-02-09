from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Post(models.Model):
    """Класс для создания записей."""

    title = models.CharField(
        max_length=150,
        verbose_name='Название поста'
        )
    text = models.TextField(
        max_length=250,
        verbose_name='Текст поста',
        null=True,
        blank=True,
        )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата публикации'
        )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts',
        verbose_name='Автор'
        )
    is_published = models.BooleanField(
        default=True,
        verbose_name='Опубликовано'
        )

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ('-pub_date',)

    def __str__(self):
        return f'Название поста {self.title}'
