from django.contrib import admin

# Register your models here.
from hotel.models import Hotel, Room, HotelOptions

admin.site.register(Hotel)
admin.site.register(Room)
admin.site.register(HotelOptions)