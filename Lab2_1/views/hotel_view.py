from rest_framework import status
from rest_framework.generics import (
    RetrieveUpdateDestroyAPIView, ListCreateAPIView, ListAPIView,
)
from rest_framework.response import Response

from Lab2_1.models.hotel import Hotel
from Lab2_1.serializers.hotel_serializer import HotelSerializer


class HotelListCreateAPIView(ListCreateAPIView):
    serializer_class = HotelSerializer
    queryset = Hotel.objects.all()


class HotelRetrieveUpdateAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = HotelSerializer
    queryset = Hotel.objects.all()


