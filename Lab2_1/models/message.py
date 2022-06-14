from django.db import models

from Lab2_1.models.client import Client
from Lab2_1.models.hotel import Hotel


class Message(models.Model):
    message = models.CharField(max_length=90, null=True)
    rate = models.CharField(max_length=90, null=True)
    date = models.CharField(max_length=90, null=True)
    hotel_id = models.ForeignKey(Hotel, on_delete=models.CASCADE, null=True)
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE, null=True)



