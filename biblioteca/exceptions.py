class BibliotecaError(Exception):
    """Excepción base para todos los errores de la biblioteca."""
    pass

class LibroSinStockError(BibliotecaError):
    """Se dispara cuando no quedan ejemplares disponibles para reservar."""
    pass

class SocioInactivoError(BibliotecaError):
    """Se dispara cuando un socio inactivo intenta realizar una operación."""
    pass

class ReservaInvalidaError(BibliotecaError):
    """Se dispara al intentar cancelar, retirar o devolver una reserva en estado incorrecto."""
    pass

class ElementoNoEncontradoError(BibliotecaError):
    """Se dispara cuando se busca un Libro o Socio que no existe en la base de datos."""
    pass

