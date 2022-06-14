from rest_framework import serializers
from Lab2_1.models.message import Message


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'