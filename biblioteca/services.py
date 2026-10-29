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
            raise DatoInvalido("El email no es válido")
    if Socio.objects.filter(numero_socio=numero_socio).exists():
            raise NumeroSocioDuplicado("Ya existe un socio con el número " + str(numero_socio))
    if Socio.objects.filter(dni=dni).exists():
            raise DniDuplicado("Ya existe un socio con el DNI " + dni)

    socio = Socio.objects.create(
        numero_socio=numero_socio,
        nombre=nombre,
        apellido=apellido,
        dni=dni,
        email=email,
    )
    return socio

def listar_socios():
    return Socio.objects.all().order_by("numero_socio")

def socios_activos():
    return Socio.objects.filter(activo=True).order_by("numero_socio")

def buscar_socio(numero_socio):
    socio = Socio.objects.filter(numero_socio=numero_socio).first()
    if socio is None:
        raise SocioNoEncontrado("No existe un socio con el número " + str(numero_socio))
    return socio

# Reservas
def reservar_libro(socio, libro):
    #El socio tiene que estar activo
    if not socio.puede_reservar():
        raise SocioInactivo("El socio está inactivo y no puede hacer reservas")
     #No se puede tener una reserva del mismo libro
    reservas_activas = Reserva.objects.filter(
            socio=socio,
            libro=libro,
            estado__in=[Reserva.PENDIENTE, Reserva.RETIRADA],
        )
    if reservas_activas.exists():
            raise ReservaDuplicada("El socio ya tiene una reserva activa de este libro")
    #Tiene que haber libros
    libro.reservar_ejemplar()
    
    reserva = Reserva.objects.create(socio=socio, libro=libro)
    return reserva

def buscar_reserva(numero_reserva):
    reserva = Reserva.objects.filter(id=numero_reserva).first()
    if reserva is None:
        raise ReservaNoEncontrada("No existe la reserva N° " + str(numero_reserva))
    return reserva
#El "-" ordena de la más nueva a la más vieja
def listar_reservas():
    return Reserva.objects.all().order_by("-fecha_reserva")

def reservas_pendientes():
    return Reserva.objects.filter(estado=Reserva.PENDIENTE).order_by("-fecha_reserva")