from rest_framework.serializers import ModelSerializer

from habit.models import Condition, Reward, Habit


class ConditionSerializer(ModelSerializer):
    """Сериализатор для модели Condition."""
    class Meta:
        model = Condition
        fields = "__all__"


class RewardSerializer(ModelSerializer):
    """Сериализатор для модели Reward."""
    class Meta:
        model = Reward
        fields = "__all__"


class HabitSerializer(ModelSerializer):
    """Сериализатор для модели Habit."""
    # condition = ConditionSerializer(many=False)
    # reward = RewardSerializer(many=False)

    class Meta:
        model = Habit
        fields = "__all__"
