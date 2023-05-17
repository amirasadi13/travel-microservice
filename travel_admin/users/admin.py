from django.contrib import admin

# Register your models here.
from users.models import User, FlightProviderOperator, HotelOperator, HotelSupervisor

admin.site.register(User)
admin.site.register(FlightProviderOperator)
admin.site.register(HotelOperator)
admin.site.register(HotelSupervisor)