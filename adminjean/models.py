from django.contrib.auth.models import User
from django.db import models


class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    nacionalidad = models.CharField(max_length=50, blank=True, null=True)

    fecha_registro = models.DateTimeField(auto_now_add=True)
    datos_extra = models.JSONField(blank=True, null=True)

    def __str__(self):
        return str(self.nombre)


class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=150, blank=True, null=True)

    fecha_registro = models.DateTimeField(auto_now_add=True)
    datos_extra = models.JSONField(blank=True, null=True)

    def __str__(self):
        return str(self.nombre)


class Libro(models.Model):
    titulo = models.CharField(max_length=150)
    isbn = models.CharField(max_length=20, unique=True)
    anio_publicacion = models.PositiveIntegerField()

    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    fecha_registro = models.DateTimeField(auto_now_add=True)
    datos_extra = models.JSONField(blank=True, null=True)

    def __str__(self):
        return str(self.titulo)


class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=150, blank=True, null=True)
    telefono = models.CharField(max_length=15)
    correo = models.EmailField(unique=True)

    fecha_registro = models.DateTimeField(auto_now_add=True)
    datos_extra = models.JSONField(blank=True, null=True)

    def __str__(self):
        return str(self.nombre)


class Prestamo(models.Model):
    ESTADOS = [
        ("ACTIVO", "Activo"),
        ("DEVUELTO", "Devuelto"),
        ("ATRASADO", "Atrasado"),
    ]

    fecha_prestamo = models.DateField()
    fecha_devolucion = models.DateField(blank=True, null=True)
    estado = models.CharField(max_length=10, choices=ESTADOS)

    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    fecha_registro = models.DateTimeField(auto_now_add=True)
    datos_extra = models.JSONField(blank=True, null=True)

    def __str__(self):
        return f"Prestamo {self.pk}"


class DetallePrestamo(models.Model):
    prestamo = models.ForeignKey(Prestamo, on_delete=models.CASCADE)

    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)

    cantidad = models.PositiveIntegerField(default=1)

    fecha_registro = models.DateTimeField(auto_now_add=True)
    datos_extra = models.JSONField(blank=True, null=True)

    def __str__(self):
        return f"{self.libro.titulo} ({self.cantidad})"
