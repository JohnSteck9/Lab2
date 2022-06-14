from django.db import models

from Lab2_1.models.hotel import Hotel


class HotelChain(models.Model):
    name = models.CharField(max_length=30, null=False)
    hotel_id = models.ForeignKey(Hotel, on_delete=models.CASCADE, null=True)


    # def synk_insurance_to_user(self, user, available_status):
    #     self.reserved_by_user = user
    #     self.is_available = available_status
    #     return True
