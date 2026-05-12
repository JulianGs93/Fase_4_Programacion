from cliente import Cliente
from servicio import ReservaSala, AlquilerEquipo, AsesoriaEspecializada
from reserva import Reserva
from excepciones import ErrorValidacion, ErrorCliente, ErrorReserva
from logger import configurar_logger


# =========================
# CONFIGURAR LOGGER
# =========================
logger = configurar_logger()


def ejecutar():
    logger.info("Inicio del sistema Software FJ")

    # =========================
    # 1. CLIENTE VÁLIDO
    # =========================
    try:
        cliente1 = Cliente("Juan Perez", "12345", "juan@mail.com")
        print(cliente1.mostrar_informacion())
    except Exception as e:
        logger.error(e)

    # =========================
    # 2. CLIENTE INVÁLIDO
    # =========================
    try:
        cliente2 = Cliente("Al", "12ab", "correo_invalido")
    except Exception as e:
        logger.error(f"Error creando cliente: {e}")

    # =========================
    # 3. SERVICIOS
    # =========================
    sala = ReservaSala("Sala A", 10)
    equipo = AlquilerEquipo("Proyector", "VideoBeam")
    asesoria = AsesoriaEspecializada("Consultoría", "Dr. Smith")

    # =========================
    # 4. RESERVA EXITOSA
    # =========================
    try:
        reserva1 = Reserva(cliente1, sala, 3)
        reserva1.procesar()
        reserva1.confirmar()
        print(reserva1.mostrar_detalle())
    except Exception as e:
        logger.error(e)

    # =========================
    # 5. RESERVA FALLIDA (duración inválida)
    # =========================
    try:
        reserva2 = Reserva(cliente1, equipo, 0)
        reserva2.procesar()
    except Exception as e:
        logger.error(f"Error en reserva: {e}")

    # =========================
    # 6. RESERVA ASERORÍA
    # =========================
    try:
        reserva3 = Reserva(cliente1, asesoria, 2)
        reserva3.procesar()
        print(reserva3.mostrar_detalle())
    except Exception as e:
        logger.error(e)

    # =========================
    # 7. CANCELAR RESERVA
    # =========================
    try:
        reserva3.cancelar()
        print("Reserva cancelada")
    except Exception as e:
        logger.error(e)

    # =========================
    # 8. ERROR SERVICIO
    # =========================
    try:
        servicio_invalido = AlquilerEquipo("Equipo X", "")
        reserva4 = Reserva(cliente1, servicio_invalido, 2)
        reserva4.procesar()
    except Exception as e:
        logger.error(f"Error servicio: {e}")

    # =========================
    # 9. OTRO CLIENTE VÁLIDO
    # =========================
    try:
        cliente3 = Cliente("Maria Lopez", "98765", "maria@mail.com")
        print(cliente3.mostrar_informacion())
    except Exception as e:
        logger.error(e)

    # =========================
    # 10. RESERVA FINAL
    # =========================
    try:
        reserva_final = Reserva(cliente3, sala, 5)
        reserva_final.procesar()
        reserva_final.confirmar()
        print(reserva_final.mostrar_detalle())
    except Exception as e:
        logger.error(e)

    logger.info("Fin del sistema Software FJ")


# =========================
# EJECUCIÓN
# =========================
if __name__ == "__main__":
    ejecutar()
