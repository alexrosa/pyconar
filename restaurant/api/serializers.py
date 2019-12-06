from rest_framework import serializers
from api.models import Reservation


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Reservation