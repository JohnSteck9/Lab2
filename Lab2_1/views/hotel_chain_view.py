from rest_framework.generics import (
    RetrieveUpdateDestroyAPIView, ListCreateAPIView, ListAPIView,
)
from Lab2_1.models.hotel_chain import HotelChain
from Lab2_1.serializers.hotel_chain_serializer import HotelChainSerializer


class HotelChainListCreateAPIView(ListCreateAPIView):
    serializer_class = HotelChainSerializer
    queryset = HotelChain.objects.all()


class HotelChainRetrieveUpdateAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = HotelChainSerializer
    queryset = HotelChain.objects.all()
