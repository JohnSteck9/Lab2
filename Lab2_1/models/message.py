from django.db import models

class Message(models.Model):
    message = models.CharField(max_length=90, null=True)
    rate = models.CharField(max_length=90, null=True)
    date = models.CharField(max_length=90, null=True)


