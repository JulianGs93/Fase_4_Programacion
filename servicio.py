from abc import ABC, abstractmethod
from excepciones import ErrorServicio, ErrorValidacion


# =========================
# CLASE ABSTRACTA SERVICIO
# =========================

class Servicio(ABC):
    """
    Clase base abstracta para todos los servicios.
    """

    def __init__(self, nombre):
        self.nombre = nombre

    @abstractmethod
    def calcular_costo(self, duracion):
        pass

    @abstractmethod
    def describir(self):
        pass

    @abstractmethod
    def validar(self):
        pass


# =========================
# SERVICIO 1: RESERVA SALA
# =========================

class ReservaSala(Servicio):

    def __init__(self, nombre, capacidad):
        super().__init__(nombre)
        self.capacidad = capacidad

    def validar(self):
        if self.capacidad <= 0:
            raise ErrorValidacion("La capacidad debe ser mayor a 0")

    def calcular_costo(self, duracion):
        self.validar()
        return duracion * 50000  # costo por hora

    def describir(self):
        return f"Reserva de sala: {self.nombre} para {self.capacidad} personas"


# =========================
# SERVICIO 2: ALQUILER EQUIPOS
# =========================

class AlquilerEquipo(Servicio):

    def __init__(self, nombre, tipo_equipo):
        super().__init__(nombre)
        self.tipo_equipo = tipo_equipo

    def validar(self):
        if not self.tipo_equipo:
            raise ErrorValidacion("Tipo de equipo inválido")

    def calcular_costo(self, duracion):
        self.validar()
        return duracion * 30000  # costo por hora

    def describir(self):
        return f"Alquiler de equipo: {self.tipo_equipo}"


# =========================
# SERVICIO 3: ASESORÍA
# =========================

class AsesoriaEspecializada(Servicio):

    def __init__(self, nombre, especialista):
        super().__init__(nombre)
        self.especialista = especialista

    def validar(self):
        if len(self.especialista) < 3:
            raise ErrorValidacion("Nombre del especialista inválido")

    def calcular_costo(self, duracion):
        self.validar()
        return duracion * 80000  # costo por hora

    def describir(self):
        return f"Asesoría especializada con {self.especialista}"
