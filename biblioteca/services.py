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
    
    libro = Libro.objects.create(
        isbn=isbn,
        titulo=titulo,
        autor=autor,
        anio_publicacion=anio_publicacion,
        cantidad_total=cantidad_total,
        cantidad_disponible=cantidad_total,
    )
    return libro


def listar_libros():
    return Libro.objects.all().order_by("titulo")


def buscar_libro_por_isbn(isbn):
    libro = Libro.objects.filter(isbn=isbn).first()
    if libro is None:
        raise LibroNoEncontrado("No existe un libro con el ISBN " + isbn)
    return libro


def buscar_libros_por_titulo(texto):
    # icontains para que no importa si esta en mayuscula o minuscula
    return Libro.objects.filter(titulo__icontains=texto).order_by("titulo")


def buscar_libros_por_autor(texto):
    return Libro.objects.filter(autor__icontains=texto).order_by("titulo")


def libros_disponibles():
    # gt = "mayor que" (greater than)
    return Libro.objects.filter(cantidad_disponible__gt=0).order_by("titulo")


def libros_sin_disponibles():
    return Libro.objects.filter(cantidad_disponible=0).order_by("titulo")

# Socios 
def registrar_socio(numero_socio, nombre, apellido, dni, email):
    if "@" not in email:
            raise DatoInvalido("El email no es válido.")
    if Socio.objects.filter(numero_socio=numero_socio).exists():
            raise NumeroSocioDuplicado("Ya existe un socio con el número " + str(numero_socio) + ".")
    if Socio.objects.filter(dni=dni).exists():
            raise DniDuplicado("Ya existe un socio con el DNI " + dni + ".")