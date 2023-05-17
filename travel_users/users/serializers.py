from rest_framework.serializers import ModelSerializer

from users.models import User, FlightProviderOperator, HotelSupervisor


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class FlightProviderOperatorSerializer(UserSerializer):
    class Meta:
        model = FlightProviderOperator
        fields = '__all__'


class HotelSupervisorSerializer(UserSerializer):
    class Meta:
        model = HotelSupervisor
        fields = '__all__'
