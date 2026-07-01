
import requests

from django.conf import settings

BASE_URL = f"https://api.telegram.org/bot{settings.BOT_TOKEN}"





def send_message(chat_id, text):

    requests.post(
        f"{BASE_URL}/sendMessage",
        json={
            "chat_id": chat_id,
            "text": text,
        },
        timeout=10
    )