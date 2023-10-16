from django.urls import path

from habits.apps import HabitConfig
from habits.views import HabitsCreateAPIView, HabitsListAPIView, HabitsRetrieveAPIView, HabitsUpdateAPIView, \
    HabitsDestroyAPIView, HabitListPublicAPIView

app_name = HabitConfig.name

urlpatterns = [
    path('habit/create/', HabitsCreateAPIView.as_view(), name='habit_create'),
    path('habit/', HabitsListAPIView.as_view(), name='habit_list'),
    path('habit/<int:pk>/', HabitsRetrieveAPIView.as_view(), name='habit_retrieve'),
    path('habit/update/<int:pk>/', HabitsUpdateAPIView.as_view(), name='habit_update'),
    path('habit/delete/<int:pk>/', HabitsDestroyAPIView.as_view(), name='habit_delete'),
    path('habit/public/', HabitListPublicAPIView.as_view(), name='habit_public'),
]
