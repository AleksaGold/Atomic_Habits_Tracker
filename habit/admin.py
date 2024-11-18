from django.contrib import admin

from habit.models import Condition, Habit, Reward


@admin.register(Condition)
class ConditionAdmin(admin.ModelAdmin):
    """Класс для настройки отображения модели "Condition" в административной панели."""

    list_display = (
        "pk",
        "place",
        "frequency",
        "seconds_to_complete",
    )


@admin.register(Reward)
class RewardAdmin(admin.ModelAdmin):
    """Класс для настройки отображения модели "Reward" в административной панели."""

    list_display = (
        "pk",
        "name",
        "owner",
    )


@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    """Класс для настройки отображения модели "Habit" в административной панели."""

    list_display = (
        "pk",
        "name",
        "owner",
        "is_pleasant",
        "is_public",
    )
