from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import User
from .serializers import UserSerializer
from events.publisher import EventPublisher

KAFKA_TOPIC = 'users_users'

event_publisher = EventPublisher()


@receiver(post_save, sender=User)
def user_create_or_update(sender, instance, **kwargs):
    print('hello')
    event_publisher.publish_data(method='create_or_update',body=UserSerializer(instance).data, route_key='user', topic=KAFKA_TOPIC)


@receiver(post_delete, sender=User)
def user_delete(sender, instance, **kwargs):
    event_publisher.publish_data(method='delete',
            body=UserSerializer(instance).data, route_key='user', topic=KAFKA_TOPIC)
