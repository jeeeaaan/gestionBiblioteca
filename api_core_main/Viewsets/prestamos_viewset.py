from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.viewsets import ModelViewSet

from adminjean.models import Prestamo
from api_core_main.Serializer.prestamos_serializer import (
    PrestamoSerializer,
)


class PrestamoViewSet(viewsets.ModelViewSet):
    queryset = Prestamo.objects.all()
    serializer_class = PrestamoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["usuario", "estado"]
