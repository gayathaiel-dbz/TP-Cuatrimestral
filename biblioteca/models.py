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