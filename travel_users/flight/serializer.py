from rest_framework import serializers

from flight.models import Flight, Airplane, Airport, FlightProvider, BookedFlight


class AirplaneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airplane
        fields = '__all__'


class AirportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airport
        fields = '__all__'


class FlightProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = FlightProvider
        fields = '__all__'


class FlightSerializer(serializers.ModelSerializer):
    flight_airplane = AirplaneSerializer(read_only=True)
    flight_airport_from = AirportSerializer(read_only=True)
    flight_airport_to = AirportSerializer(read_only=True)
    flight_provider = FlightProviderSerializer(read_only=True)

    class Meta:
        model = Flight
        fields = '__all__'


class FlightCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = '__all__'


class BookedFlightCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookedFlight
        fields = '__all__'


