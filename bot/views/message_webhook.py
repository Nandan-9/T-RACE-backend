from datetime import datetime, timezone

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..services.send_message_service import send_message

class TelegramWebhook(APIView):

    authentication_classes = []
    permission_classes = []

    def post(self, request):

        update = request.data
        message = update.get("message", {})
        sender = message.get("from", {})
        chat = message.get("chat", {})

        data = {
            "update_id": update.get("update_id"),
            "message_id": message.get("message_id"),
            "text": message.get("text"),
            "date": datetime.fromtimestamp(message["date"], tz=timezone.utc) if message.get("date") else None,
            "sender_id": sender.get("id"),
            "sender_first_name": sender.get("first_name"),
            "sender_last_name": sender.get("last_name"),
            "sender_username": sender.get("username"),
            "sender_is_bot": sender.get("is_bot"),
            "sender_language_code": sender.get("language_code"),
            "chat_id": chat.get("id"),
            "chat_type": chat.get("type"),
        }
        print(data)
        send_message(data["chat_id"],"hai daaa")


        return Response(
            {"status": "received"},
            status=status.HTTP_200_OK
        )