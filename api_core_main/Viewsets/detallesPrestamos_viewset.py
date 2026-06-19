from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.viewsets import ModelViewSet

from adminjean.models import DetallePrestamo
from api_core_main.Serializer.detallesPrestamos_serializer import (
    DetallePrestamoSerializer,
)


class DetallePrestamoViewSet(viewsets.ModelViewSet):
    queryset = DetallePrestamo.objects.all()
    serializer_class = DetallePrestamoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["prestamo", "libro"]
