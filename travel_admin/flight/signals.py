from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import Airplane, Airport, FlightProvider, Flight
from .serializer import AirplaneSerializer, AirportSerializer, FlightProviderSerializer, \
    FlightCreateSerializer
from events.publisher import EventPublisher

KAFKA_TOPIC = 'flight_users'

event_publisher = EventPublisher()


@receiver(post_save, sender=Airplane)
def airplane_create_or_update(sender, instance, **kwargs):
    event_publisher.publish_data(method='create_or_update',
            body=AirplaneSerializer(instance).data, route_key='airplane', topic=KAFKA_TOPIC)


@receiver(post_delete, sender=Airplane)
def airplane_delete(sender, instance, **kwargs):
    event_publisher.publish_data(method='delete', body=AirplaneSerializer(instance).data, route_key='airplane', topic=KAFKA_TOPIC)


@receiver(post_save, sender=Airport)
def airport_create_or_update(sender, instance, **kwargs):
    event_publisher.publish_data(method='create_or_update', body=AirportSerializer(instance).data, route_key='airport', topic=KAFKA_TOPIC)


@receiver(post_delete, sender=Airport)
def airport_delete(sender, instance, **kwargs):
    event_publisher.publish_data(method='delete', body=AirportSerializer(instance).data, route_key='airport', topic=KAFKA_TOPIC)


@receiver(post_save, sender=FlightProvider)
def flight_provider_create_or_update(sender, instance, **kwargs):
    event_publisher.publish_data(method='create_or_update', body=FlightProviderSerializer(instance).data, route_key='flight_provider', topic=KAFKA_TOPIC)


@receiver(post_delete, sender=FlightProvider)
def flight_provider_delete(sender, instance, **kwargs):
    event_publisher.publish_data(method='delete', body=FlightProviderSerializer(instance).data, route_key='flight_provider', topic=KAFKA_TOPIC)


@receiver(post_save, sender=Flight)
def flight_create_or_update(sender, instance, **kwargs):
    event_publisher.publish_data(method='create_or_update', body=FlightCreateSerializer(instance).data,
            route_key='flight', topic=KAFKA_TOPIC)


@receiver(post_delete, sender=Flight)
def flight_delete(sender, instance, **kwargs):
    event_publisher.publish_data(method='delete', body=FlightCreateSerializer(instance).data,
            route_key='flight', topic=KAFKA_TOPIC)
