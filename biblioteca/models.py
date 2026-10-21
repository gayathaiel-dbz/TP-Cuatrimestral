from django.db import models
from django.utils import timezone

from biblioteca.exceptions import CantidadInvalida, EstadoInvalido, SinDisponibilidad

class Libro(models.Model):
    isbn = models.CharField(max_length=13, unique=True)
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=150)
# No se usa "CharField" porque ese guarda texot y el "PositiveIntegerField" es un entero
    anio_publicacion = models.PositiveIntegerField()
    cantidad_total = models.PositiveIntegerField(default=1)
    cantidad_disponible = models.PositiveIntegerField(default=1)

class Socio(models.Model):
    numero_socio = models.PositiveIntegerField(unique=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    dni = models.CharField(max_length=10, unique=True)
    email = models.EmailField()
    activo = models.BooleanField(default=True)

    def __str__(self):
        if self.activo:
            estado = "Activo"
        else:
            estado = "Inactivo"
        return f"N° {self.numero_socio} - {self.apellido}, {self.nombre} (DNI {self.dni}) - {estado}"

    def puede_reservar(self):
        # Por ahora la única condición del socio es estar activo.
        return self.activo

    def activar(self):
        self.activo = True
        self.save()

    def desactivar(self):
        self.activo = False
        self.save()