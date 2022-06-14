from django.db import models

from Lab2_1.models.client import Client
from Lab2_1.models.message import Message


class Hotel(models.Model):
    name = models.CharField(max_length=30, null=True)
    stars = models.CharField(max_length=30, null=True)
    location = models.CharField(max_length=80, null=False)
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE, null=True)
    message_id = models.ForeignKey(Message, on_delete=models.CASCADE, null=True)

