from rest_framework import serializers

from adminjean.models import DetallePrestamo


class DetallePrestamoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetallePrestamo
        fields = "__all__"
