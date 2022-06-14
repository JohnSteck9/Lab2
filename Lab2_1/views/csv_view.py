import csv

from rest_framework import status
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response

from Lab2_1.models.client import Client
from Lab2_1.serializers.client_serializer import ClientSerializer


class UploadDataCSVFile(ListCreateAPIView):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()

    def create(self, request, *args, **kwargs):
        file = request.data.get('client_data')
        file_rows = [row.decode("utf-8") for row in file]
        reader = csv.reader(file_rows, quotechar='"', delimiter=',', quoting=csv.QUOTE_ALL)
        for client in reader:
            if client:
                request_data = format_data(client)
                create_request_record(request_data)  # METHOD INJECTION
        return Response('Uploaded', status=status.HTTP_201_CREATED)


def format_data(client):
    request_data = {"id": client.pop(0),
                    "first_name": client.pop(0),
                    "second_name": client.pop(0),
                    "email": client.pop(0),
                    "message_id": client.pop(0)}

    return request_data


def create_request_record(request_data):
    client_serializer = ClientSerializer(data=request_data)
    client_serializer.is_valid(raise_exception=True)
    request_obj = client_serializer.save()

    request_obj.save()

    return True
