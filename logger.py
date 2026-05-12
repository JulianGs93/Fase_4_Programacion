import logging


def configurar_logger():
    """
    Configura el sistema de logs del proyecto.
    Los mensajes se guardan en el archivo logs.txt.
    """
    logging.basicConfig(
        filename="logs.txt",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        encoding="utf-8"
    )

    return logging.getLogger("SoftwareFJ")
