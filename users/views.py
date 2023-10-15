from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from users.models import User
from habits.permissions import IsOwner
from users.serializers import UserSerializer


class UserCreateAPIView(generics.CreateAPIView):
    """Контроллер для создания пользователя"""

    serializer_class = UserSerializer


class UserListAPIView(generics.ListAPIView):
    """Контроллер для списка пользователей"""

    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]


class UserRetrieveAPIView(generics.RetrieveAPIView):
    """Контроллер для просмотра пользователя"""

    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]


class UserUpdateAPIView(generics.UpdateAPIView):
    """Контроллер для обновления пользователя"""

    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsOwner, IsAuthenticated]


class UserDestroyAPIView(generics.DestroyAPIView):
    """Контроллер для удаления пользователя"""

    queryset = User.objects.all()
    permission_classes = [IsOwner, IsAuthenticated]
