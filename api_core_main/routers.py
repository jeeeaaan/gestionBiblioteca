from rest_framework import routers

from .Viewsets.autors_viewset import AutorViewSet
from .Viewsets.categorias_viewset import CategoriaViewSet
from .Viewsets.detallesPrestamos_viewset import DetallePrestamoViewSet
from .Viewsets.libros_viewset import LibroViewSet
from .Viewsets.prestamos_viewset import PrestamoViewSet
from .Viewsets.usuarios_viewset import UsuarioViewSet

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r"Autor", AutorViewSet)
router.register(r"Categoria", CategoriaViewSet)
router.register(r"Libro", LibroViewSet)
router.register(r"Prestamo", PrestamoViewSet)
router.register(r"Usuario", UsuarioViewSet)
router.register(r"DetallePrestamo", DetallePrestamoViewSet)
