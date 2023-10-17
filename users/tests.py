from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from users.models import User


class UserTestCase(APITestCase):
    def setUp(self) -> None:
        """Подготовка данных для тестирования"""

        self.user = User.objects.create(
            email="test5@test.ru",
            password="12345",
            chat_id="1727774413")
        self.user.save()
        self.client.force_authenticate(user=self.user)

    def test_create_user(self):
        """Тест создания пользователя"""

        test_create_user = {
            "email": "test@example.com",
            'password': 'test1',
            "chat_id": "123456"
        }
        response = self.client.post(
            reverse("users:user_create"), test_create_user)
        # Проверка статус вывода списка
        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )
