from rest_framework import mixins
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated

from flight.models import Flight
from flight.serializer import FlightSerializer
from utils.pagination import BasePagination


class FlightsList(mixins.ListModelMixin, GenericAPIView):
    """
        Flights List
    """
    permission_classes = [IsAuthenticated]
    serializer_class = FlightSerializer
    pagination_class = BasePagination

    def get_queryset(self):
        return Flight.objects.filter()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

