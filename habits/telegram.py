import requests

from django.conf import settings

TOKEN = settings.TELEGRAM_TOKEN


def send_message(user, text):
    user_chat_id = user.chat_id
    response = requests.get(
        f"https://api.telegram.org/bot{TOKEN}/sendMessage", {
            "chat_id": user_chat_id,
            "text": text
        }
    )
    return response.json()
