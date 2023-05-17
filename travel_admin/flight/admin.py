from django.contrib import admin

# Register your models here.
from flight.models import Flight, FlightProvider, Airport, Airplane, BookedFlight

admin.site.register(Flight)
admin.site.register(Airport)
admin.site.register(Airplane)
admin.site.register(FlightProvider)
admin.site.register(BookedFlight)
