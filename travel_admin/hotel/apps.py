from django.apps import AppConfig


class HotelConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'hotel'

    def ready(self):
        from . import signals
        # from .consumer import KafkaEvent
        # KafkaEvent(daemon=True).start()