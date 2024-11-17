
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

from habit.models import Habit, Condition, Reward
from habit.paginators import CustomPagination
from habit.serializers import HabitSerializer, ConditionSerializer, RewardSerializer, HabitDetailSerializer
from users.permissions import IsOwnerPermission


class ConditionViewSet(ModelViewSet):
    """Вьюсет для работы с моделью Condition."""
    queryset = Condition.objects.all()
    serializer_class = ConditionSerializer
    pagination_class = CustomPagination


class RewardViewSet(ModelViewSet):
    """Вьюсет для работы с моделью Reward."""
    queryset = Reward.objects.all()
    serializer_class = RewardSerializer
    pagination_class = CustomPagination

    def get_permissions(self):
        """Возвращает список разрешений, в зависимости от прав доступа."""
        if self.action == "create":
            self.permission_classes = (IsAuthenticated,)
        elif self.action in ["update", "partial_update", "retrieve", "list", "destroy"]:
            self.permission_classes = (
                IsAuthenticated & IsOwnerPermission | IsAdminUser,
            )
        return super().get_permissions()

    def perform_create(self, serializer):
        """Переопределение метода для автоматической привязки владельца к создаваемому объекту."""
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        """Возвращает объекты, в зависимости от прав доступа."""
        if self.request.user.is_superuser:
            return Reward.objects.all()
        else:
            return Reward.objects.filter(owner=self.request.user.id)


class RewardReadOnlyViewSet(ReadOnlyModelViewSet):
    """Вьюсет только для просмотра модели Reward."""
    queryset = Reward.objects.filter(is_public=True)
    serializer_class = RewardSerializer
    pagination_class = CustomPagination


class HabitViewSet(ModelViewSet):
    """Вьюсет для работы с моделью Habit."""
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    pagination_class = CustomPagination

    def get_permissions(self):
        """Возвращает список разрешений, в зависимости от прав доступа."""
        if self.action == "create":
            self.permission_classes = (IsAuthenticated,)
        elif self.action in ["update", "partial_update", "retrieve", "list", "destroy"]:
            self.permission_classes = (
                IsAuthenticated & IsOwnerPermission | IsAdminUser,
            )
        return super().get_permissions()

    def perform_create(self, serializer):
        """Переопределение метода для автоматической привязки владельца к создаваемому объекту."""
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        """Возвращает объекты, в зависимости от прав доступа."""
        if self.request.user.is_superuser:
            return Habit.objects.all()
        else:
            return Habit.objects.filter(owner=self.request.user.id)

    def get_serializer_class(self):
        """Возвращает класс сериализатора, который будет использоваться для обработки текущего запроса."""
        if self.action == "retrieve":
            return HabitDetailSerializer
        return HabitSerializer


class HabitReadOnlyViewSet(ReadOnlyModelViewSet):
    """Вьюсет только для просмотра модели Habit."""
    queryset = Habit.objects.filter(is_public=True)
    serializer_class = HabitSerializer
    pagination_class = CustomPagination
