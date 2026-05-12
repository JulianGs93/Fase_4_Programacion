from abc import ABC, abstractmethod


class Entidad(ABC):
    """
    Clase abstracta base para todas las entidades del sistema.
    """

    @abstractmethod
    def mostrar_informacion(self):
        """
        Método abstracto que debe ser implementado por las clases hijas.
        """
        pass
