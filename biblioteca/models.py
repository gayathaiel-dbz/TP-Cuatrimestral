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

    def __str__(self):
        return f"{self.titulo} - {self.autor} (ISBN {self.isbn}) - Disponibles: {self.cantidad_disponible}/{self.cantidad_total}"

    def esta_disponible(self):
        return self.cantidad_disponible > 0

    def reservar_ejemplar(self):
        # Baja la cantidad del ejemplar en 1, y no pude quedar abajo de 0.
        if not self.esta_disponible():
            raise SinDisponibilidad("No hay ejemplares de este libro.")
        self.cantidad_disponible = self.cantidad_disponible - 1
        self.save()

    def liberar_ejemplar(self):
        # Suma un ejemplar.
        if self.cantidad_disponible >= self.cantidad_total:
            raise CantidadInvalida("La cantidad no puede superar la cantidad total.")
        self.cantidad_disponible = self.cantidad_disponible + 1
        self.save()

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
        return self.activo

    def activar(self):
        self.activo = True
        self.save()

    def desactivar(self):
        self.activo = False
        self.save()
        
class Reserva(models.Model):
    # Posibles estados de una reserva
    PENDIENTE = "PENDIENTE"
    RETIRADA = "RETIRADA"
    CANCELADA = "CANCELADA"
    FINALIZADA = "FINALIZADA"

    ESTADOS = [
        (PENDIENTE, "Pendiente"),
        (RETIRADA, "Retirada"),
        (CANCELADA, "Cancelada"),
        (FINALIZADA, "Finalizada"),
    ]

    # muchas reservas pertenecen a un socio o a un libro.
    # "related_name" hace socio.reservas.all() o libro.reservas.all() para ver todas las reservas
    # "on_delete=models.PROTECT" no deja borrar un socio o un libro que tenga reservas
    socio = models.ForeignKey(Socio, on_delete=models.PROTECT, related_name="reservas")
    libro = models.ForeignKey(Libro, on_delete=models.PROTECT, related_name="reservas")
    fecha_reserva = models.DateTimeField(default=timezone.now)
    estado = models.CharField(max_length=10, choices=ESTADOS, default=PENDIENTE)