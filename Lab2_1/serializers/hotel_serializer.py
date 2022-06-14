from rest_framework import serializers
from Lab2_1.models.hotel import Hotel


class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = '__all__'