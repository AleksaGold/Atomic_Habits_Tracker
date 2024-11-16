from rest_framework.exceptions import ValidationError


def validate_compensation(value):
    """Исключает одновременный выбор связанной привычки и указания вознаграждения."""
    reward = dict(value).get("reward", "exists")
    associated_habit = dict(value).get("associated_habit", "exists")
    if associated_habit and reward:
        raise ValidationError("Нельзя выбирать приятную привычку и вознаграждение одновременно")


def validate_associated_habit(value):
    """Проверяет, что в связанные привычки могут попадать только привычки с признаком приятной привычки."""
    associated_habit = dict(value).get("associated_habit")
    if associated_habit and not associated_habit.is_pleasant:
        raise ValidationError("Связанная привычка должна быть приятной")


def validate_pleasant_habit(value):
    """Проверяет что у приятной привычки нет вознаграждения или связанной привычки."""
    is_pleasant = dict(value).get("is_pleasant", "exists")
    associated_habit = dict(value).get("associated_habit", "exists")
    reward = dict(value).get("reward", "exists")
    if is_pleasant and (associated_habit or reward):
        raise ValidationError("Приятная привычка не может быть связана с другой приятной привычкой или вознаграждением")
