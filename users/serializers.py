from rest_framework.serializers import ModelSerializer

from users.models import User


class UserSerializer(ModelSerializer):
    """Сериализатор для модели User."""

    class Meta:
        model = User
        fields = (
            "id",
            "is_superuser",
            "email",
            "tg_chat_id",
            "is_active",
        )
