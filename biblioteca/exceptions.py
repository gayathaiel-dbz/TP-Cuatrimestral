class ErrorBiblioteca(Exception):
    pass

class DatoInvalido(ErrorBiblioteca):
    pass

class LibroNoEncontrado(ErrorBiblioteca):
    pass

class SocioNoEncontrado(ErrorBiblioteca):
    pass

class ReservaNoEncontrada(ErrorBiblioteca):
    pass

class IsbnDuplicado(ErrorBiblioteca):
    pass

class DniDuplicado(ErrorBiblioteca):
    pass

class NumeroSocioDuplicado(ErrorBiblioteca):
    pass

class SinDisponibilidad(ErrorBiblioteca):
    pass

class CantidadInvalida(ErrorBiblioteca):
    pass

class SocioInactivo(ErrorBiblioteca):
    pass

class ReservaDuplicada(ErrorBiblioteca):
    pass

class EstadoInvalido(ErrorBiblioteca):
    pass