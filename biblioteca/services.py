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