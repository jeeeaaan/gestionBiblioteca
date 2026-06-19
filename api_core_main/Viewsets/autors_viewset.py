from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.viewsets import ModelViewSet

from adminjean.models import Autor
from api_core_main.Serializer.autors_serializer import AutorSerializer


class AutorViewSet(viewsets.ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    filter_backends = [DjangoFilterBackend]
    sfilterset_fields = ["nombre", "nacionalidad"]
