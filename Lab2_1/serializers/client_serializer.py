from rest_framework import serializers

from Lab2_1.models.client import Client


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'