from django.core.management.base import BaseCommand
from biblioteca import services
from biblioteca.exceptions import ErrorBiblioteca

class Command(BaseCommand):
    help = "Inicia el menú interactivo del Sistema de Reserva de Libros de la Biblioteca."

    def handle(self, *args, **options):
        while True:
            print("\n" + "=" * 45)
            print("     SISTEMA DE GESTIÓN DE BIBLIOTECA")
            print("=" * 45)
            print("1. Registrar libro")
            print("2. Registrar socio")
            print("3. Listar libros")
            print("4. Buscar libro (por ISBN, título o autor)")
            print("5. Listar socios")
            print("6. Realizar reserva")
            print("7. Cancelar reserva")
            print("8. Retirar libro reservado")
            print("9. Devolver libro")
            print("10. Listar reservas de un socio (historial)")
            print("11. Listar todas las reservas")
            print("12. Activar / desactivar socio")
            print("13. Consultas especiales")
            print("0. Salir")
            print("=" * 45)

            opcion = input("Seleccione una opción: ").strip()

            if opcion == "0":
                print("\n¡Gracias por utilizar el sistema de biblioteca!")
                break

            try:
                if opcion == "1":
                    isbn = input("ISBN: ").strip()
                    titulo = input("Título: ").strip()
                    autor = input("Autor: ").strip()
                    anio = int(input("Año de publicación: "))
                    cantidad = int(input("Cantidad total de ejemplares: "))
                    libro = services.registrar_libro(isbn, titulo, autor, anio, cantidad)
                    print(f"\n✅ Libro registrado correctamente: {libro}")

                elif opcion == "2":
                    num_socio = int(input("Número de socio: "))
                    nombre = input("Nombre: ").strip()
                    apellido = input("Apellido: ").strip()
                    dni = input("DNI: ").strip()
                    email = input("Email: ").strip()
                    socio = services.registrar_socio(num_socio, nombre, apellido, dni, email)
                    print(f"\n✅ Socio registrado correctamente: {socio}")

                elif opcion == "3":
                    libros = services.Libro.objects.all()
                    print("\n--- LISTADO DE LIBROS ---")
                    if not libros:
                        print("No hay libros registrados.")
                    for lib in libros:
                        print(f"- {lib}")

                elif opcion == "4":
                    criterio = input("Ingrese ISBN, título o autor a buscar: ").strip()
                    resultados = services.buscar_libro(criterio)
                    print("\n--- RESULTADOS DE LA BÚSQUEDA ---")
                    if not resultados:
                        print("No se encontraron coincidencias.")
                    for lib in resultados:
                        print(f"- {lib}")

                elif opcion == "5":
                    socios = services.Socio.objects.all()
                    print("\n--- LISTADO DE SOCIOS ---")
                    if not socios:
                        print("No hay socios registrados.")
                    for soc in socios:
                        print(f"- {soc}")

                elif opcion == "6":
                    num_socio = int(input("Número de socio: "))
                    isbn = input("ISBN del libro a reservar: ").strip()
                    reserva = services.reservar_libro(num_socio, isbn)
                    print(f"\n✅ Reserva creada con éxito: {reserva}")

                elif opcion == "7":
                    reserva_id = int(input("Número ID de la reserva a cancelar: "))
                    reserva = services.obtener_reserva_por_id(reserva_id)
                    reserva.cancelar()
                    print(f"\n✅ Reserva N° {reserva_id} cancelada correctamente.")

                elif opcion == "8":
                    reserva_id = int(input("Número ID de la reserva a retirar: "))
                    reserva = services.obtener_reserva_por_id(reserva_id)
                    reserva.retirar()
                    print(f"\n✅ Libro de la reserva N° {reserva_id} retirado con éxito.")

                elif opcion == "9":
                    reserva_id = int(input("Número ID de la reserva a devolver: "))
                    reserva = services.obtener_reserva_por_id(reserva_id)
                    reserva.finalizar()
                    print(f"\n✅ Libro devuelto. Reserva N° {reserva_id} finalizada.")

                elif opcion == "10":
                    num_socio = int(input("Número de socio: "))
                    historial = services.obtener_historial_socio(num_socio)
                    print(f"\n--- HISTORIAL DE RESERVAS DEL SOCIO N° {num_socio} ---")
                    if not historial:
                        print("El socio no posee reservas registradas.")
                    for res in historial:
                        print(f"- {res}")

                elif opcion == "11":
                    reservas = services.Reserva.objects.all().order_by('-fecha_reserva')
                    print("\n--- TODAS LAS RESERVAS EN EL SISTEMA ---")
                    if not reservas:
                        print("No hay reservas registradas en el sistema.")
                    for res in reservas:
                        print(f"- {res}")

                elif opcion == "12":
                    num_socio = int(input("Número de socio: "))
                    estado_str = input("¿Desea activarlo (1) o desactivarlo (0)?: ").strip()
                    activo = estado_str == "1"
                    socio = services.cambiar_estado_socio(num_socio, activo)
                    estado_txt = "activado" if socio.activo else "desactivado"
                    print(f"\n✅ Socio N° {num_socio} {estado_txt} correctamente.")

                elif opcion == "13":
                    print("\n--- SUBMENÚ DE CONSULTAS ---")
                    print("a. Libros disponibles")
                    print("b. Libros sin ejemplares")
                    print("c. Reservas pendientes")
                    print("d. Socios activos")
                    sub_op = input("Seleccione consulta (a-d): ").strip().lower()

                    if sub_op == "a":
                        for lib in services.obtener_libros_disponibles():
                            print(f"- {lib}")
                    elif sub_op == "b":
                        for lib in services.obtener_libros_sin_ejemplares():
                            print(f"- {lib}")
                    elif sub_op == "c":
                        for res in services.obtener_reservas_pendientes():
                            print(f"- {res}")
                    elif sub_op == "d":
                        for soc in services.obtener_socios_activos():
                            print(f"- {soc}")
                    else:
                        print("Sub-opción inválida.")

                else:
                    print("⚠️ Opción inválida. Intente nuevamente.")

            except ValueError:
                print("⚠️ Error: Debe ingresar un valor numérico válido.")
            except ErrorBiblioteca as e:
                print(f"⚠️ Error de sistema: {e}")

