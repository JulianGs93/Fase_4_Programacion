from excepciones import ErrorReserva, ErrorValidacion


class Reserva:
    """
    Clase que representa una reserva dentro del sistema Software FJ.
    Integra Cliente y Servicio.
    """

    def __init__(self, cliente, servicio, duracion):
        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.estado = "Pendiente"
        self.costo = 0

        self.validar_reserva()

    # ---------------- VALIDACIÓN ---------------- #

    def validar_reserva(self):
        if self.duracion <= 0:
            raise ErrorValidacion("La duración debe ser mayor a 0")

        if self.cliente is None:
            raise ErrorReserva("La reserva debe tener un cliente válido")

        if self.servicio is None:
            raise ErrorReserva("La reserva debe tener un servicio válido")

    # ---------------- PROCESOS ---------------- #

    def procesar(self):
        try:
            self.costo = self.servicio.calcular_costo(self.duracion)
            self.estado = "Procesada"
        except Exception as e:
            raise ErrorReserva("Error al procesar la reserva") from e

    def confirmar(self):
        if self.estado != "Procesada":
            raise ErrorReserva("No se puede confirmar una reserva no procesada")

        self.estado = "Confirmada"

    def cancelar(self):
        self.estado = "Cancelada"

    # ---------------- INFORMACIÓN ---------------- #

    def mostrar_detalle(self):
        return (
            f"Reserva:\n"
            f"Cliente: {self.cliente.nombre}\n"
            f"Servicio: {self.servicio.nombre}\n"
            f"Duración: {self.duracion}\n"
            f"Estado: {self.estado}\n"
            f"Costo: {self.costo}"
        )
