from rest_framework import status
from rest_framework.generics import (
    RetrieveUpdateDestroyAPIView, ListCreateAPIView, ListAPIView,
)
from rest_framework.response import Response

from Lab2_1.models.client import Client
from Lab2_1.serializers.client_serializer import ClientSerializer


class ClientListCreateAPIView(ListCreateAPIView):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()

    def create(self, request, *args, **kwargs):
        request_data = request.data.copy()
        request_serializer = self.get_serializer(data=request_data)
        request_serializer.is_valid(raise_exception=True)
        request_obj = request_serializer.save()
        request_obj.email = "some randommmmmmmmmmmmmmmmmm"
        request_obj.save()
        return Response(request_serializer.data, status=status.HTTP_201_CREATED)


class ClientRetrieveUpdateAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()


