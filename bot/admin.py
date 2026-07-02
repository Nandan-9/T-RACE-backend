from django.contrib import admin

from bot.models import Botlogs


@admin.register(Botlogs)
class BotlogsAdmin(admin.ModelAdmin):
    list_display = (
        "message_id",
        "chat_id",
        "chat_type",
        "sender_first_name",
        "response_message_text",
        "is_sender_bot",
    )
