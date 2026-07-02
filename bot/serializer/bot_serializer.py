from rest_framework import serializers
from ..models import Botlogs



class BotLogSerializer(serializers.ModelSerializer):

    class Meta:
        model = Botlogs
        fields = "__all__"





