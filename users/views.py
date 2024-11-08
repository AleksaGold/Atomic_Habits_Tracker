from rest_framework.viewsets import ModelViewSet

from users.models import User
from users.serializers import UserSerializer


class UserViewSet(ModelViewSet):
    """Вьюсет для работы с моделью User."""

    queryset = User.objects.all()
    serializer_class = UserSerializer
