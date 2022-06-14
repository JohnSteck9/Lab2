from rest_framework import status
from rest_framework.generics import (
    RetrieveUpdateDestroyAPIView, ListCreateAPIView, ListAPIView,
)
from rest_framework.response import Response

from Lab2_1.models.message import Message
from Lab2_1.serializers.message_serializer import MessageSerializer


class MessageListCreateAPIView(ListCreateAPIView):
    serializer_class = MessageSerializer
    queryset = Message.objects.all()


class MessageRetrieveUpdateAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = MessageSerializer
    queryset = Message.objects.all()


