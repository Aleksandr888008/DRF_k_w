from rest_framework import status
from rest_framework.test import APITestCase

from habits.models import Habit
from users.models import User

from django.urls import reverse


class HabitTestCase(APITestCase):
    """Тестирование CRUD привычки."""

    def setUp(self) -> None:
        """Подготовка данных для тестирования"""
        self.password = "user"

        self.user = User.objects.create(
            email="test@test.ru",
            chat_id="1234"
        )
        self.user.set_password(self.password)
        self.user.save()

        self.user_2 = User.objects.create(
            email="test1@test.ru",
            chat_id="12345"
        )
        self.user_2.set_password(self.password)
        self.user_2.save()

        response = self.client.post(
            reverse("users:token_obtain_pair"),
            {"email": self.user.email, "password": self.password}
        )

        self.token = response.json().get("access")
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')

        self.test_habit_data = {
            "owner": self.user,
            "action": "test",
            "place": "test",
            "time": "00:00:00",
            "period": 3,
            "execution_time": "00:00:10"
        }

        self.habit = Habit.objects.create(**self.test_habit_data)

    def test_list_habits(self):
        """Тестирование вывода списка привычек"""
        response = self.client.get(
            reverse("habits:habit_list")
        )
        # Проверка статус вывода списка
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_update_habits(self):
        """Тестирование обновления привычки автором"""
        test_habit_update = {
            "place": "car"
        }

        response = self.client.patch(
            reverse("habits:habit_update", args=[self.habit.pk]),
            test_habit_update
        )
        # Проверка статус вывода списка
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_update_habits_not_owner(self):
        """Тестирование обновления привычки не автором"""
        response = self.client.post(
            reverse("users:token_obtain_pair"),
            {"email": self.user_2.email, "password": self.password}
        )

        self.token = response.json().get("access")
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')

        test_habit_update = {
            "place": "car"
        }

        response = self.client.patch(
            reverse("habits:habit_update", args=[self.habit.pk]), test_habit_update)
        # Проверка статус вывода списка
        self.assertEqual(
            response.status_code,
            status.HTTP_403_FORBIDDEN
        )

    def test_create_habits(self):
        """Тестирование создания привычки"""
        test_create_data = {
            "owner": self.user.pk,
            "action": "test1",
            "place": "test1",
            "time": "00:01:00",
            "period": 1,
            "execution_time": "00:01:10"
        }

        response = self.client.post(
            reverse("habits:habit_create"), test_create_data)
        # Проверка статус вывода списка
        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

    def test_retrieve_habits(self):
        """Тестирование вывода данных по отдельной привычки"""
        response = self.client.get(reverse('habits:habit_retrieve', args=[self.habit.pk]))
        # print(response.json())
        # Проверка статус вывода списка
        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_delete_habits(self):
        """Тестирование удаления привычки"""
        response = self.client.delete(reverse('habits:habit_delete', args=[self.habit.pk]))
        # Проверяем статус вывода списка
        self.assertEquals(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

    def test_list_public_habit(self):
        """Тестирование списка публичных привычек"""
        response = self.client.get(reverse('habits:habit_public'))
        # Проверяем статус вывода списка
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
