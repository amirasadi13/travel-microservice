from .models import Airplane, Airport, Flight, FlightProvider
from .serializer import AirplaneSerializer, AirportSerializer, FlightProviderSerializer, FlightCreateSerializer


class FlightItemCallbackHandler:
    def __init__(self, route_key, data, method):
        self.data = data
        self.method = method
        print(route_key)
        self._get_item_instance_by_route_key(route_key)

    def item_create_or_update(self, instance, serializer_instance):
        try:
            item = instance.objects.get(id=self.data['id'])
            serializer = serializer_instance(instance=item, data=self.data)
            if serializer.is_valid():
                serializer.save()
            else:
                pass
        except instance.DoesNotExist:
            serializer = serializer_instance(data=self.data)
            if serializer.is_valid():
                serializer.id = self.data['id']
                serializer.save()
            else:
                pass

    def item_delete(self, instance):
        try:
            instance.objects.get(id=self.data['id']).delete()
        except instance.DoesNotExist:
            pass

    def _get_item_instance_by_route_key(self, route_key):
        if route_key == 'airplane':
            self._get_action_method(self.method, Airplane, AirplaneSerializer)
        elif route_key == 'airport':
            self._get_action_method(self.method, Airport, AirportSerializer)
        elif route_key == 'flight':
            self._get_action_method(self.method, Flight, FlightCreateSerializer)
        elif route_key == 'flight_provider':
            self._get_action_method(self.method, FlightProvider, FlightProviderSerializer)

    def _get_action_method(self, method, instance, serializer_instance):
        if method == 'create_or_update':
            self.item_create_or_update(instance, serializer_instance)
        elif method == 'delete':
            self.item_delete(instance)
