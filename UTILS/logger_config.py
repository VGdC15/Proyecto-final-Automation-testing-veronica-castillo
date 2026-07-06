import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parents[1]
LOGS_DIR = ROOT_DIR / "logs"
LOG_FILE = LOGS_DIR / "automation.log"


def configurar_logger():
    """Configura un logger centralizado para toda la suite de automatización."""
    LOGS_DIR.mkdir(exist_ok=True)

    logger = logging.getLogger("automation")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    if logger.handlers:
        return logger

    formatter = logging.Formatter(
        fmt="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    file_handler = RotatingFileHandler(
        LOG_FILE,
        maxBytes=1_000_000,
        backupCount=3,
        encoding="utf-8",
    )
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    return logger


def obtener_logger(nombre="automation"):
    """Devuelve un logger hijo del logger principal."""
    configurar_logger()
    return logging.getLogger(nombre)