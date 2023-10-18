import requests

from django.conf import settings

TOKEN = settings.TELEGRAM_TOKEN


def send_message(user, text):
    """Подготовка для отправки сообщения в телеграм"""
    user_chat_id = user.chat_id
    response = requests.get(
        f"https://api.telegram.org/bot{TOKEN}/sendMessage", {
            "chat_id": user_chat_id,
            "text": text
        }
    )
    return response.json()


def update_chat_id():
    """Получение chat_id пользователей"""
    response = requests.get(f"https://api.telegram.org/bot{TOKEN}/getUpdates").json()
    if response.get("ok"):
        user_chats = []  # Получение списка
        for ch_id in response.get("result"):
            chat_id = ch_id.get("message").get("chat").get("id")
            user_chats.append(chat_id)
