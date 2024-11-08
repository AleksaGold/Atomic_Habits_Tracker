from rest_framework.viewsets import ModelViewSet

from habit.models import Habit, Condition, Reward
from habit.serializers import HabitSerializer, ConditionSerializer, RewardSerializer


class ConditionViewSet(ModelViewSet):
    """Вьюсет для работы с моделью Condition."""
    queryset = Condition.objects.all()
    serializer_class = ConditionSerializer
    

class RewardViewSet(ModelViewSet):
    """Вьюсет для работы с моделью Reward."""
    queryset = Reward.objects.all()
    serializer_class = RewardSerializer


class HabitViewSet(ModelViewSet):
    """Вьюсет для работы с моделью Habit."""
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
