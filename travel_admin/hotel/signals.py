from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import Room, HotelOptions, Hotel
from .serializers import RoomSerializer, HotelSerializer, HotelOptionsSerializer
from events.publisher import EventPublisher

KAFKA_TOPIC = 'hotel_users'

event_publisher = EventPublisher()


@receiver(post_save, sender=Room)
def room_create_or_update(sender, instance, **kwargs):
    event_publisher.publish_data(method='create_or_update',
            body=RoomSerializer(instance).data, route_key='room', topic=KAFKA_TOPIC)


@receiver(post_delete, sender=Room)
def room_delete(sender, instance, **kwargs):
    event_publisher.publish_data(method='delete', body=RoomSerializer(instance).data, route_key='room', topic=KAFKA_TOPIC)


@receiver(post_save, sender=Hotel)
def hotel_create_or_update(sender, instance, **kwargs):
    print(HotelSerializer(instance).data)
    event_publisher.publish_data(method='create_or_update',
            body=HotelSerializer(instance).data, route_key='hotel', topic=KAFKA_TOPIC)


@receiver(post_delete, sender=Hotel)
def hotel_delete(sender, instance, **kwargs):
    event_publisher.publish_data(method='delete', body=HotelSerializer(instance).data, route_key='hotel', topic=KAFKA_TOPIC)


@receiver(post_save, sender=HotelOptions)
def hotel_option_create_or_update(sender, instance, **kwargs):
    event_publisher.publish_data(method='create_or_update',
            body=HotelOptionsSerializer(instance).data, route_key='hotel_option', topic=KAFKA_TOPIC)


@receiver(post_delete, sender=HotelOptions)
def hotel_option_delete(sender, instance, **kwargs):
    event_publisher.publish_data(method='delete', body=HotelOptionsSerializer(instance).data, route_key='hotel_option', topic=KAFKA_TOPIC)

