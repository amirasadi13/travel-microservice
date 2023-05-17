from .models import BookedFlight
from .serializer import BookedFlightCreateSerializer


class FlightItemCallbackHandler:
    def __init__(self, route_key, data, method):
        self.data = data
        self.method = method
        self._get_item_instance_by_route_key(route_key)

    def item_create_or_update(self, instance, serializer_instance):
        try:
            item = instance.objects.get(id=self.data['id'])
            serializer = serializer_instance(instance=item, data=self.data)
            if serializer.is_valid():
                serializer.save()
            else:
                print(serializer.errors)
        except instance.DoesNotExist:
            serializer = serializer_instance(data=self.data)
            if serializer.is_valid():
                serializer.id = self.data['id']
                serializer.save()
            else:
                print(serializer.errors)

    def item_delete(self, instance):
        try:
            instance.objects.get(id=self.data['id']).delete()
        except instance.DoesNotExist:
            pass

    def _get_item_instance_by_route_key(self, route_key):
        if route_key == 'booked_flight':
            self._get_action_method(self.method, BookedFlight, BookedFlightCreateSerializer)

    def _get_action_method(self, method, instance, serializer_instance):
        if method == 'create_or_update':
            self.item_create_or_update(instance, serializer_instance)
        elif method == 'delete':
            self.item_delete(instance)
