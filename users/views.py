from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated

from users.models import User
from users.permissions import IsUserPermission
from users.serializers import UserSerializer


class UserViewSet(ModelViewSet):
    """Вьюсет для работы с моделью User."""

    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        """Создает и возвращает список разрешений, требуемых для регистрации пользователя."""
        if self.action == "create":
            self.permission_classes = (AllowAny,)
        elif self.action in ["update", "partial_update"]:
            self.permission_classes = (
                IsAuthenticated & IsUserPermission | IsAdminUser,
            )
        elif self.action in ["list", "retrieve"]:
            self.permission_classes = (IsAuthenticated,)
        else:
            self.permission_classes = (IsAuthenticated & IsAdminUser,)
        return super().get_permissions()

    def perform_create(self, serializer):
        """Сохраняет сериализованные данные при регистрации пользователя и хэширует пароль."""
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()
