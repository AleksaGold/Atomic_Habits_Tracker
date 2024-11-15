from rest_framework.exceptions import ValidationError


def validate_compensation(value):
    """Исключает одновременный выбор связанной привычки и указания вознаграждения."""
    if value.get("reward") and value.get("associated_habit"):
        raise ValidationError("Нельзя выбирать приятную привычку и вознаграждение одновременно")


def validate_associated_habit(value):
    """Проверяет, что в связанные привычки могут попадать только привычки с признаком приятной привычки."""
    tmp_value = dict(value).get("associated_habit")
    if tmp_value and not tmp_value.is_pleasant:
        raise ValidationError("Связанная привычка должна быть приятной")


def validate_pleasant_habit(value):
    """Проверяет что у приятной привычки нет вознаграждения или связанной привычки."""
    if value.get("is_pleasant") and (value.get("associated_habit") or value.get("reward")):
        raise ValidationError("Приятная привычка не может быть связана с другой приятной привычкой или вознаграждением")

