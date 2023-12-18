from rest_framework import serializers
from .models import Airplane

class AirplaneSerializer(serializers.ModelSerializer):
    fuel_consumption_per_minute: float = serializers.SerializerMethodField()
    max_minutes_fly: float = serializers.SerializerMethodField()

    class Meta:
        model = Airplane
        fields = ['plane_id', 'passenger_assumptions', 'fuel_consumption_per_minute', 'max_minutes_fly']

    def get_fuel_consumption_per_minute(self, obj) -> float:
        return round(obj.fuel_consumption_per_minute(), 2)

    def get_max_minutes_fly(self, obj) -> float:
        return round(obj.max_minutes_fly(), 2)