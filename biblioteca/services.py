from biblioteca.exceptions import (
    DatoInvalido,
    DniDuplicado,
    IsbnDuplicado,
    LibroNoEncontrado,
    NumeroSocioDuplicado,
    ReservaDuplicada,
    ReservaNoEncontrada,
    SocioInactivo,
    SocioNoEncontrado,
    CantidadInvalida,
)
from biblioteca.models import Libro, Reserva, Socio

# Libros
def registrar_libro(isbn, titulo, autor, anio_publicacion, cantidad_total):
    if len(isbn) > 13:
        raise DatoInvalido("El ISBN no puede tener mas de 13 caracteres")
    if cantidad_total < 1:
        raise CantidadInvalida("El libro debe tener al menos 1 ejemplar")
    if Libro.objects.filter(isbn=isbn).exists():
        raise IsbnDuplicado("Ya existe un libro con el ISBN " + isbn)

def listar_libros():
    return Libro.objects.all().order_by("titulo")


def buscar_libro_por_isbn(isbn):


def buscar_libros_por_titulo(texto):


def buscar_libros_por_autor(texto):


def libros_disponibles():


def libros_sin_disponibles():
    return Libro.objects.filter(cantidad_disponible=0).order_by("titulo")