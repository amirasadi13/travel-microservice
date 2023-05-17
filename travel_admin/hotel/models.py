from django.db import models

from base.models import BaseModel


class Hotel(BaseModel):
    title = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    address_text = models.TextField(null=True, blank=True)
    address_latitude_deg = models.CharField(max_length=50, blank=True, null=True)
    address_longitude_deg = models.CharField(max_length=50, blank=True, null=True)
    options = models.ManyToManyField('HotelOptions', related_name='hotel_options', blank=True)

    def __str__(self):
        return self.title


class Room(BaseModel):
    title = models.CharField(max_length=200, null=True, blank=True)
    bed_count = models.PositiveIntegerField(null=True, blank=True)
    price_per_night = models.PositiveIntegerField(null=True, blank=True)
    capacity = models.PositiveIntegerField(null=True, blank=True)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.title}'


class HotelOptions(BaseModel):
    title = models.CharField(max_length=250, null=True, blank=True)
    is_enable = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.title}'


class BookedRoom(BaseModel):
    pass
