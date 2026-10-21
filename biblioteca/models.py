from django.db import models
from django.utils import timezone

from biblioteca.exceptions import CantidadInvalida, EstadoInvalido, SinDisponibilidad

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
