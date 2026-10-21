class BibliotecaError(Exception):
    pass

class LibroSinStockError(BibliotecaError):
    pass

class SocioInactivoError(BibliotecaError):
    pass

class ReservaInvalidaError(BibliotecaError):
    pass

class ElementoNoEncontradoError(BibliotecaError):
    pass

