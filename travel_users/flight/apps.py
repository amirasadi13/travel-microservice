from django.apps import AppConfig


class FlightConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'flight'

    def ready(self):
        from . import signals
