from rest_framework import serializers
from Lab2_1.models.hotel_chain import HotelChain


class HotelChainSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelChain
        fields = '__all__'