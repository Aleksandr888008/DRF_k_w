from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from habits.models import Habit
from habits.paginators import ListPaginator
from habits.serializers import HabitSerializer, HabitCreateSerializer
from habits.permissions import IsOwner


class HabitsCreateAPIView(generics.CreateAPIView):
    """Создание привычки"""
    serializer_class = HabitCreateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        new_habit = serializer.save()
        new_habit.user = self.request.user
        new_habit.save()


class HabitsListAPIView(generics.ListAPIView):
    """Просмотр своих привычек"""
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated | IsOwner]
    pagination_class = ListPaginator

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)


class HabitsRetrieveAPIView(generics.RetrieveAPIView):
    """Детальный просмотр привычки"""
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated | IsOwner]


class HabitsUpdateAPIView(generics.UpdateAPIView):
    """Изменение привычки"""
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated | IsOwner]


class HabitsDestroyAPIView(generics.DestroyAPIView):
    """Удаление привычки"""
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated | IsOwner]


class HabitListPublicAPIView(generics.ListAPIView):
    """Просмотр публичных привычек"""
    queryset = Habit.objects.filter(is_public=True)
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = ListPaginator
