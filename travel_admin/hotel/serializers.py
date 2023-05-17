from rest_framework import serializers

from .models import BookedRoom, Room, HotelOptions, Hotel


class BookedRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookedRoom
        fields = '__all__'


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'


class HotelOptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelOptions
        fields = '__all__'


class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = '__all__'

