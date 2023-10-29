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

# def get_chat_id(user) -> str | None:
#
#     response = requests.get(f"https://api.telegram.org/bot{TOKEN}/getUpdates").json()
#     if response.get("ok"):
#         for update in response["result"]:
#             if update["message"]["chat"]["username"] == user.tg_username:
#                 return update["message"]["chat"]["id"]
