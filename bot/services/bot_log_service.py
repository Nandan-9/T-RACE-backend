from ..serializer.bot_serializer import BotLogSerializer


def log_bot_messages(data, message_response):
    payload = {**data, "response_message_text": message_response}
    serializer = BotLogSerializer(data=payload)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return serializer.instance



 

















                       