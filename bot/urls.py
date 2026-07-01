from django.urls import path



from .views.message_webhook import TelegramWebhook


urlpatterns = [
    path("webhook/",TelegramWebhook.as_view()),
]


