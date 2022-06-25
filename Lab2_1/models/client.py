from django.db import models
from Lab2_1.models.message import Message

class Client(models.Model):
    first_name = models.CharField(max_length=30, null=False)
    second_name = models.CharField(max_length=30, null=False)
    email = models.CharField(max_length=90, null=True)
    message_id = models.ForeignKey(Message, on_delete=models.CASCADE, null=True)

