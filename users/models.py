from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {"blank": True, "null": True}


class User(AbstractUser):
    """Модель User для хранения информации о пользователях веб-приложения."""

    username = None
    email = models.EmailField(unique=True, verbose_name="Email")

    avatar = models.ImageField(
        upload_to="users/avatars", verbose_name="Аватар", **NULLABLE
    )
    token = models.CharField(max_length=100, verbose_name="Токен", **NULLABLE)
    tg_nickname = models.CharField(
        max_length=50, verbose_name="Telegram ник", **NULLABLE
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        """Возвращает строковое представление объекта."""
        return self.email

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
