from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from django.http import HttpResponse
from typing import List
from .models import Airplane
from .serializers import AirplaneSerializer

# Create your views here.

class AirplaneViewSet(viewsets.ModelViewSet):
    queryset: List[Airplane] = Airplane.objects.all()
    serializer_class: Serializer = AirplaneSerializer

    def list(self, request, *args, **kwargs) -> HttpResponse:
        queryset: List[Airplane] = self.filter_queryset(self.get_queryset())
        serializer: Serializer = self.get_serializer(queryset, many=True)

        # Add calculated value to each serialized instance
        for i, instance_data in enumerate(serializer.data):
            instance: Airplane = queryset[i]
            max_minutes_fly: float = instance.max_minutes_fly()
            fuel_consumption_per_minute: float = instance.fuel_consumption_per_minute()
            serializer.data[i]['max_minutes_fly'] = round(max_minutes_fly, 2)
            serializer.data[i]['fuel_consumption_per_minute'] = round(fuel_consumption_per_minute, 2)

        return Response(serializer.data)