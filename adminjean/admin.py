from django.contrib import admin

from .models import Autor, Categoria, DetallePrestamo, Libro, Prestamo, Usuario

admin.site.register(Libro)
admin.site.register(Autor)
admin.site.register(Prestamo)
admin.site.register(DetallePrestamo)
admin.site.register(Usuario)
admin.site.register(Categoria)
