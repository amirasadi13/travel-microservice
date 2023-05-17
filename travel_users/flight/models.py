from django.db import models

from base.models import BaseModel
from constants import constants
from users.models import User


class Flight(BaseModel):
    FLIGHT_TYPE = (
        (constants.ECONOMY, constants.ECONOMY),
        (constants.BUSINESS, constants.BUSINESS),
    )
    FLIGHT_DESTINATION_TYPE = (
        (constants.INTERNAL, constants.INTERNAL),
        (constants.EXTERNAL, constants.EXTERNAL),
    )
    title = models.CharField(max_length=100, null=True, blank=True)
    flight_provider = models.ForeignKey('FlightProvider', on_delete=models.CASCADE, null=True, blank=True)
    flight_type = models.CharField(choices=FLIGHT_TYPE, default=constants.ECONOMY, max_length=10)
    flight_destination_type = models.CharField(choices=FLIGHT_DESTINATION_TYPE, default=constants.INTERNAL, max_length=15)
    flight_price = models.PositiveBigIntegerField(null=True, blank=True)
    flight_ticket_count = models.PositiveIntegerField(null=True, blank=True)
    flight_landing_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    flight_takeoff_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    flight_waiting_on_destination_airport_time = models.TimeField(null=True, blank=True)
    flight_duration = models.TimeField(null=True, blank=True)
    flight_airport_from = models.ForeignKey('Airport', related_name='airport_from', on_delete=models.CASCADE, null=True, blank=True)
    flight_airport_to = models.ForeignKey('Airport', related_name='airport_to', on_delete=models.CASCADE, null=True, blank=True)
    flight_maximum_load_weight = models.PositiveIntegerField(null=True, blank=True)
    flight_roles = models.TextField(null=True, blank=True)
    flight_number = models.CharField(max_length=10, null=True, blank=True)
    flight_airplane = models.ForeignKey('Airplane', related_name='flight_airplane', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.flight_airport_from}  --->  {self.flight_airport_to}'


class FlightProvider(BaseModel):
    title = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.title}'


class Airport(BaseModel):
    name = models.CharField(max_length=250, null=True, blank=True)
    indent = models.CharField(max_length=25, null=True, blank=True)
    type = models.CharField(max_length=20, null=True, blank=True)
    latitude_deg = models.CharField(max_length=50, blank=True, null=True)
    longitude_deg = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f'{self.name} - {self.type}'


class Airplane(BaseModel):
    airplane_name = models.CharField(max_length=200, null=True, blank=True)
    airplane_model = models.CharField(max_length=100, null=True, blank=True)
    airplane_body_class = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return f'{self.airplane_name}'


class BookedFlight(BaseModel):
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE, null=True, blank=True)
    customer = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    booked_date = models.DateTimeField(null=True, blank=True)
    payment_date = models.DateTimeField(null=True, blank=True)
    payment_ref_id = models.CharField(max_length=100, blank=True, null=True)
    ticket_count = models.PositiveIntegerField(null=True, blank=True)
    