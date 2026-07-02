
import requests
from django.conf import settings
from ..llm.llm_services import generate_response


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


def ans_to_query(question):

    if not question:
        return "Sorry I am not able to answer at the moment"
    
    # response = generate_response(question=question)
    response = "under-development please cooperate"
    return response
