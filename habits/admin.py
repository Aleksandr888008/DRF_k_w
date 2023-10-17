from django.contrib import admin

from habits.models import Habit


@admin.register(Habit)
class HabitsAdmin(admin.ModelAdmin):
    list_display = ["owner", "place", "time"]  # отображение на дисплее
    list_filter = ["owner"]  # фильтр
    search_fields = ["owner"]  # поля поиска
