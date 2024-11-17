from rest_framework.serializers import ModelSerializer

from habit.models import Condition, Reward, Habit
from habit.validators import validate_compensation, validate_associated_habit, validate_pleasant_habit


class ConditionSerializer(ModelSerializer):
    """Сериализатор для модели Condition."""
    class Meta:
        model = Condition
        fields = (
            "id",
            "place",
            "start_time",
            "frequency",
            "seconds_to_complete",
        )


class RewardSerializer(ModelSerializer):
    """Сериализатор для модели Reward."""
    class Meta:
        model = Reward
        fields = (
            "id",
            "name",
            "owner",
            "is_public",
        )


class HabitSerializer(ModelSerializer):
    """Сериализатор для модели Habit."""

    class Meta:
        model = Habit
        fields = (
            "id",
            "name",
            "owner",
            "is_pleasant",
            "is_public",
            "associated_habit",
            "reward",
            "condition",
        )

        validators = [validate_compensation, validate_associated_habit, validate_pleasant_habit]


class HabitDetailSerializer(ModelSerializer):
    """Сериализатор для одного объекта Habit."""
    condition = ConditionSerializer(read_only=True)

    class Meta:
        model = Habit
        fields = "__all__"
