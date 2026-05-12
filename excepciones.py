class ErrorSistema(Exception):
    """Clase base para todas las excepciones del sistema."""
    pass


class ErrorValidacion(ErrorSistema):
    """Error generado cuando los datos no cumplen las reglas de validación."""
    pass


class ErrorCliente(ErrorSistema):
    """Error relacionado con la creación o gestión de clientes."""
    pass


class ErrorServicio(ErrorSistema):
    """Error relacionado con la creación o gestión de servicios."""
    pass


class ErrorReserva(ErrorSistema):
    """Error relacionado con la creación o procesamiento de reservas."""
    pass
