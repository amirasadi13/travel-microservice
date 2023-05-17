from django.urls import path

from flight.views import FlightsList

app_name = 'flight'

urlpatterns = [
    path('flight/', FlightsList.as_view(), name='flightsList'),
]
