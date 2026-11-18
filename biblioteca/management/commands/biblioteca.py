from django.core.management.base import BaseCommand
from biblioteca import services
from biblioteca.exceptions import ErrorBiblioteca


# ---------------------------------------------------------------
# Funciones de ayuda para pedir datos
# ---------------------------------------------------------------

def pedir_texto(mensaje):
    # Pide un texto y vuelve a preguntar si el usuario lo deja vacío.
    while True:
        texto = input(mensaje).strip()
        if texto != "":
            return texto
        print("Este dato no puede quedar vacío.")


def pedir_numero(mensaje):
    # Pide un número entero (0 o mayor) y vuelve a preguntar si no lo es.
    while True:
        texto = input(mensaje).strip()
        try:
            numero = int(texto)
        except ValueError:
            print("Tiene que ingresar un número.")
            continue
        if numero < 0:
            print("El número no puede ser negativo.")
            continue
        return numero


def mostrar_lista(elementos, mensaje_si_esta_vacia):
    if len(elementos) == 0:
        print(mensaje_si_esta_vacia)
        return
    for elemento in elementos:
        print(elemento)


# ---------------------------------------------------------------
# Una función por cada opción del menú
# ---------------------------------------------------------------

def registrar_libro():
    print("\n--- Registrar libro ---")
    isbn = pedir_texto("ISBN: ")
    titulo = pedir_texto("Título: ")
    autor = pedir_texto("Autor: ")
    anio = pedir_numero("Año de publicación: ")
    cantidad = pedir_numero("Cantidad de ejemplares: ")
    libro = services.registrar_libro(isbn, titulo, autor, anio, cantidad)
    print("Libro registrado correctamente:", libro)


def registrar_socio():
    print("\n--- Registrar socio ---")
    numero = pedir_numero("Número de socio: ")
    nombre = pedir_texto("Nombre: ")
    apellido = pedir_texto("Apellido: ")
    dni = pedir_texto("DNI: ")
    email = pedir_texto("Email: ")
    socio = services.registrar_socio(numero, nombre, apellido, dni, email)
    print("Socio registrado correctamente:", socio)


def listar_libros():
    print("\n--- Libros ---")
    mostrar_lista(services.listar_libros(), "No hay libros registrados.")


def buscar_libro():
    print("\n--- Buscar libro ---")
    print("1. Por ISBN")
    print("2. Por título")
    print("3. Por autor")
    opcion = input("Seleccione una opción: ").strip()

    if opcion == "1":
        isbn = pedir_texto("ISBN: ")
        libro = services.buscar_libro_por_isbn(isbn)
        print(libro)
    elif opcion == "2":
        texto = pedir_texto("Título (o parte del título): ")
        mostrar_lista(services.buscar_libros_por_titulo(texto), "No se encontraron libros.")
    elif opcion == "3":
        texto = pedir_texto("Autor (o parte del nombre): ")
        mostrar_lista(services.buscar_libros_por_autor(texto), "No se encontraron libros.")
    else:
        print("Opción inválida.")


def listar_socios():
    print("\n--- Socios ---")
    mostrar_lista(services.listar_socios(), "No hay socios registrados.")


def realizar_reserva():
    print("\n--- Realizar reserva ---")
    numero_socio = pedir_numero("Número de socio: ")
    socio = services.buscar_socio(numero_socio)
    isbn = pedir_texto("ISBN del libro: ")
    libro = services.buscar_libro_por_isbn(isbn)
    reserva = services.reservar_libro(socio, libro)
    print("Reserva realizada correctamente:", reserva)


def cancelar_reserva():
    print("\n--- Cancelar reserva ---")
    numero = pedir_numero("Número de reserva: ")
    reserva = services.buscar_reserva(numero)
    reserva.cancelar()
    print("Reserva cancelada:", reserva)


def retirar_libro():
    print("\n--- Retirar libro reservado ---")
    numero = pedir_numero("Número de reserva: ")
    reserva = services.buscar_reserva(numero)
    reserva.retirar()
    print("Libro retirado:", reserva)


def devolver_libro():
    print("\n--- Devolver libro ---")
    numero = pedir_numero("Número de reserva: ")
    reserva = services.buscar_reserva(numero)
    reserva.finalizar()
    print("Libro devuelto:", reserva)


def listar_reservas_de_socio():
    print("\n--- Reservas de un socio ---")
    numero_socio = pedir_numero("Número de socio: ")
    socio = services.buscar_socio(numero_socio)
    print("Historial de", socio)
    mostrar_lista(services.reservas_de_socio(socio), "El socio no tiene reservas.")


def listar_todas_las_reservas():
    print("\n--- Todas las reservas ---")
    mostrar_lista(services.listar_reservas(), "No hay reservas registradas.")


def activar_o_desactivar_socio():
    print("\n--- Activar / desactivar socio ---")
    numero_socio = pedir_numero("Número de socio: ")
    socio = services.buscar_socio(numero_socio)
    if socio.activo:
        socio.desactivar()
        print("El socio ahora está INACTIVO.")
    else:
        socio.activar()
        print("El socio ahora está ACTIVO.")


def consultas():
    print("\n--- Consultas ---")
    print("1. Libros disponibles")
    print("2. Libros sin ejemplares disponibles")
    print("3. Reservas pendientes")
    print("4. Reservas de un libro")
    print("5. Socios activos")
    opcion = input("Seleccione una opción: ").strip()

    if opcion == "1":
        mostrar_lista(services.libros_disponibles(), "No hay libros disponibles.")
    elif opcion == "2":
        mostrar_lista(services.libros_sin_disponibles(), "Todos los libros tienen ejemplares disponibles.")
    elif opcion == "3":
        mostrar_lista(services.reservas_pendientes(), "No hay reservas pendientes.")
    elif opcion == "4":
        isbn = pedir_texto("ISBN del libro: ")
        libro = services.buscar_libro_por_isbn(isbn)
        mostrar_lista(services.reservas_de_libro(libro), "El libro no tiene reservas.")
    elif opcion == "5":
        mostrar_lista(services.socios_activos(), "No hay socios activos.")
    else:
        print("Opción inválida.")


def mostrar_menu():
    print()
    print("=============================")
    print("         BIBLIOTECA")
    print("=============================")
    print("1. Registrar libro")
    print("2. Registrar socio")
    print("3. Listar libros")
    print("4. Buscar libro")
    print("5. Listar socios")
    print("6. Realizar reserva")
    print("7. Cancelar reserva")
    print("8. Retirar libro reservado")
    print("9. Devolver libro")
    print("10. Listar reservas de un socio")
    print("11. Listar todas las reservas")
    print("12. Activar / desactivar socio")
    print("13. Consultas")
    print("0. Salir")


# ---------------------------------------------------------------
# El comando de Django
# ---------------------------------------------------------------

class Command(BaseCommand):
    help = "Inicia el sistema de biblioteca"

    def handle(self, *args, **options):
        print("Sistema de biblioteca iniciado")

        while True:
            mostrar_menu()
            try:
                opcion = input("Seleccione una opción: ").strip()

                if opcion == "1":
                    registrar_libro()
                elif opcion == "2":
                    registrar_socio()
                elif opcion == "3":
                    listar_libros()
                elif opcion == "4":
                    buscar_libro()
                elif opcion == "5":
                    listar_socios()
                elif opcion == "6":
                    realizar_reserva()
                elif opcion == "7":
                    cancelar_reserva()
                elif opcion == "8":
                    retirar_libro()
                elif opcion == "9":
                    devolver_libro()
                elif opcion == "10":
                    listar_reservas_de_socio()
                elif opcion == "11":
                    listar_todas_las_reservas()
                elif opcion == "12":
                    activar_o_desactivar_socio()
                elif opcion == "13":
                    consultas()
                elif opcion == "0":
                    print("Saliendo del sistema...")
                    break
                else:
                    print("Opción inválida.")

            except ErrorBiblioteca as error:
                # Errores esperables: libro inexistente, socio inactivo, etc.
                print("Error:", error)
            except (KeyboardInterrupt, EOFError):
                # El usuario apretó Ctrl+C o se terminó la entrada.
                print("\nSaliendo del sistema...")
                break
            except Exception as error:
                # Cualquier otro problema: lo mostramos y el programa sigue.
                print("Ocurrió un error inesperado:", error)
