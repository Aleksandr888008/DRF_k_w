from rest_framework import generics, response, status
from rest_framework.permissions import IsAuthenticated, AllowAny
from users.models import User
from habits.permissions import IsOwner
from users.serializers import UserSerializer


class UserCreateAPIView(generics.CreateAPIView):
    """Контроллер для создания пользователя"""

    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        password = serializer.data["password"]
        user = User.objects.get(email=serializer.data['email'])
        user.set_password(password)
        user.save()

        return response.Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


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
