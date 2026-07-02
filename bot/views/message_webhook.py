from datetime import datetime, timezone

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..services import message_services 
from ..services import bot_log_service

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
            "message_text": message.get("text"),
            "message_date": datetime.fromtimestamp(message["date"], tz=timezone.utc) if message.get("date") else None,
            "sender_id": sender.get("id"),
            "sender_first_name": sender.get("first_name"),
            "sender_last_name": sender.get("last_name"),
            "is_sender_bot": sender.get("is_bot"),
            "sender_lang_code": sender.get("language_code"),
            "chat_id": chat.get("id"),
            "chat_type": chat.get("type"),
        }

        if data["message_text"] is not None:
            response = message_services.ans_to_query(data["message_text"])
            message_services.send_message(data["chat_id"], response)
            bot_log_service.log_bot_messages(data, response)


        return Response(
            {"status": "received"},
            status=status.HTTP_200_OK
        )