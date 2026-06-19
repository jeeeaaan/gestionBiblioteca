from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.viewsets import ModelViewSet

from adminjean.models import Categoria
from api_core_main.Serializer.categorias_serializer import (
    CategoriaSerializer,
)


class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["nombre", "descripcion"]
