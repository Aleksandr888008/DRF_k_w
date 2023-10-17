from django.contrib import admin

from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["email", "phone", "chat_id"]  # отображение на дисплее
    list_filter = ["email", "chat_id"]  # фильтр
    search_fields = ["email", "phone", "chat_id"]  # поля поиска
