from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import BookedRoom
from .serializers import BookedRoomSerializer

from events.publisher import EventPublisher

KAFKA_TOPIC = 'hotel_admin'


event_publisher = EventPublisher()


@receiver(post_save, sender=BookedRoom)
def booked_room_create_or_update(sender, instance, **kwargs):
    event_publisher.publish_data(method='create_or_update',
            body=BookedRoomSerializer(instance).data, route_key='booked_room', topic=KAFKA_TOPIC)


@receiver(post_delete, sender=BookedRoom)
def booked_room_delete(sender, instance, **kwargs):
    event_publisher.publish_data(method='delete', body=BookedRoomSerializer(instance).data, route_key='booked_room', topic=KAFKA_TOPIC)

