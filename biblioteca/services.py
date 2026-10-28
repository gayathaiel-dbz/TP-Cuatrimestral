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


def listar_libros():


def buscar_libro_por_isbn(isbn):


def buscar_libros_por_titulo(texto):


def buscar_libros_por_autor(texto):


def libros_disponibles():


def libros_sin_disponibles():