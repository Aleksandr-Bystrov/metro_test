from datetime import date

from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.validators import MaxValueValidator
from django.db import models

from metro.settings import MAX_LENGH_BIO, MAX_LENGH_EMAIL, MAX_LENGH_NAME


class CustomUser(AbstractUser):
    """Модель пользователя."""

    username = models.CharField(
        validators=[UnicodeUsernameValidator()],
        unique=True,
        max_length=MAX_LENGH_NAME,
    )
    email = models.EmailField(max_length=MAX_LENGH_EMAIL, unique=True)
    avatar = models.ImageField(
        upload_to='avatars',
        null=True,
        default=None
    )
    first_name = models.CharField(
        ('Имя'),
        max_length=MAX_LENGH_NAME,
    )
    last_name = models.CharField(
        ('Фамилия'),
        max_length=MAX_LENGH_NAME,
    )
    bio = models.CharField(
        ('Биография'),
        null=True,
        max_length=MAX_LENGH_BIO
    )
    date_of_birth = models.DateField(
        null=True,
        validators=[MaxValueValidator(
            limit_value=date.today,
            message='Дата рождения не может быть в будущем.')],
    )

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['username']

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
