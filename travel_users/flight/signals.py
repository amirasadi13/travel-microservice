from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import BookedFlight
from .serializer import BookedFlightCreateSerializer

from events.publisher import EventPublisher

KAFKA_TOPIC = 'flight_admin'


event_publisher = EventPublisher()


@receiver(post_save, sender=BookedFlight)
def booked_flight_create_or_update(sender, instance, **kwargs):
    event_publisher.publish_data(method='create_or_update', body=BookedFlightCreateSerializer(instance).data, route_key='booked_flight', topic=KAFKA_TOPIC)


@receiver(post_delete, sender=BookedFlight)
def booked_flight_delete(sender, instance, **kwargs):
    event_publisher.publish_data(method='delete', body=BookedFlightCreateSerializer(instance).data, route_key='booked_flight', topic=KAFKA_TOPIC)
