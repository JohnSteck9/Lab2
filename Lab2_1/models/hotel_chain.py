from django.db import models
from Lab2_1.models.hotel import Hotel

class HotelChain(models.Model):
    name = models.CharField(max_length=30, null=False)
    hotel_id = models.ForeignKey(Hotel, on_delete=models.CASCADE, null=True)

