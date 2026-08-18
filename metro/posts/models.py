from django.db import models

from users.models import CustomUser
from metro.settings import MAX_NAME_POST


class Post(models.Model):
    """Модель поста."""

    content = models.TextField('Текст')
    created_at = models.DateTimeField(
        verbose_name='Дата и время публикации',
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        verbose_name='Дата и время изменения публикации',
        auto_now=True
    )
    author = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        verbose_name='Автор публикации'
    )
    image = models.ImageField(
        'Изображение', upload_to='posts_images', blank=True)

    class Meta:
        verbose_name = 'публикация'
        verbose_name_plural = 'Публикации'
        default_related_name = 'posts'

    def __str__(self):
        return self.content[:MAX_NAME_POST]
