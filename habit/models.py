from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from config import settings

NULLABLE = {"blank": True, "null": True}


class Condition(models.Model):
    """Класс для описания модели Conditions."""

    place = models.CharField(max_length=150, verbose_name="Место выполнения")
    start_time = models.TimeField(
        auto_now=False, verbose_name="Время начала выполнения привычки"
    )
    frequency = models.PositiveSmallIntegerField(
        verbose_name="Периодичность выполнения в днях",
        default=1,
        validators=[MaxValueValidator(7), MinValueValidator(1)],
    )
    seconds_to_complete = models.PositiveSmallIntegerField(
        validators=[MaxValueValidator(120)], verbose_name="Время на выполнение привычки"
    )

    class Meta:
        verbose_name = "Условие выполнения привычки"
        verbose_name_plural = "Условия выполнения привычек"
        ordering = ("frequency", "start_time")

    def __str__(self):
        """Возвращает строковое представление объекта."""
        return f"{self.place} {self.frequency} {self.start_time}"


class Reward(models.Model):
    """Класс для описания модели Reward."""

    name = models.CharField(max_length=150, verbose_name="Название вознаграждения")
    description = models.TextField(verbose_name="Описание вознаграждения", **NULLABLE)
    preview = models.ImageField(
        upload_to="rewards/previews", verbose_name="Превью (картинка)", **NULLABLE
    )
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        verbose_name="Владелец вознаграждения",
        **NULLABLE,
        related_name="rewards",
    )

    is_public = models.BooleanField(
        default=False, verbose_name="Публичное вознаграждение"
    )

    class Meta:
        verbose_name = "Вознаграждение"
        verbose_name_plural = "Вознаграждения"
        ordering = ("name",)

    def __str__(self):
        """Возвращает строковое представление объекта."""
        return f"{self.name}"


class Habit(models.Model):
    """Класс для описания модели Habit."""

    name = models.CharField(max_length=150, verbose_name="Название привычки")
    description = models.TextField(
        verbose_name="Описание привычки", **NULLABLE
    )
    preview = models.ImageField(
        upload_to="habits/previews", verbose_name="Превью (картинка)", **NULLABLE
    )
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        verbose_name="Владелец привычки",
        **NULLABLE,
        related_name="habits",
    )
    is_pleasant = models.BooleanField(default=False, verbose_name="Приятная привычка")
    is_public = models.BooleanField(default=False, verbose_name="Публичная привычка")
    associated_habit = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        verbose_name="Связанная привычка",
        **NULLABLE,
        related_name="habits",
    )
    reward = models.ForeignKey(
        "habit.Reward",
        on_delete=models.CASCADE,
        verbose_name="Вознаграждение",
        **NULLABLE,
        related_name="habits",
    )

    condition = models.ForeignKey(
        "habit.Condition",
        on_delete=models.CASCADE,
        verbose_name="Условия выполнения привычки",
        related_name="habits",
    )
    next_sending = models.DateTimeField(
        auto_now=False,
        verbose_name="Дата следующей отправки уведомления в Telegram",
        **NULLABLE,
    )

    class Meta:
        verbose_name = "Привычка"
        verbose_name_plural = "Привычки"
        ordering = ("name",)

    def __str__(self):
        """Возвращает строковое представление объекта."""
        return f"{self.name} ({self.associated_habit} {self.reward})"
