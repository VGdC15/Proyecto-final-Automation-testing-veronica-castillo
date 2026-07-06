from datetime import datetime
from pathlib import Path
import re

import pytest
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

from utils.data_reader import obtener_datos_prueba


ROOT_DIR = Path(__file__).resolve().parent
SCREENSHOTS_DIR = ROOT_DIR / "screenshots"


@pytest.fixture(scope="function")
def driver():
    """Crea y cierra una instancia de Chrome WebDriver para cada test."""
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    service = Service()
    navegador = webdriver.Chrome(service=service, options=chrome_options)

    yield navegador

    try:
        navegador.quit()
    except WebDriverException:
        pass


@pytest.fixture(scope="session")
def datos_prueba():
    """Carga los datos externos de prueba una sola vez por sesión."""
    return obtener_datos_prueba()


@pytest.fixture
def credenciales_validas(datos_prueba):
    """Devuelve credenciales válidas desde archivo JSON."""
    return datos_prueba["usuarios"]["valido"]


@pytest.fixture
def credenciales_invalidas(datos_prueba):
    """Devuelve el primer set de credenciales inválidas desde archivo JSON."""
    return datos_prueba["usuarios"]["invalidos"][0]


@pytest.fixture
def usuario_bloqueado(datos_prueba):
    """Devuelve el usuario bloqueado desde archivo JSON."""
    return datos_prueba["usuarios"]["invalidos"][1]


@pytest.fixture
def datos_checkout(datos_prueba):
    """Devuelve los datos de checkout desde archivo JSON."""
    return datos_prueba["checkout"]


def _normalizar_nombre_test(nombre_test):
    """Limpia el nombre del test para usarlo como nombre de archivo."""
    return re.sub(r"[^a-zA-Z0-9_-]", "_", nombre_test)


def guardar_screenshot(driver, nombre_test):
    """Guarda una captura de pantalla con fecha, hora y nombre del test."""
    SCREENSHOTS_DIR.mkdir(exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    nombre_limpio = _normalizar_nombre_test(nombre_test)
    ruta_screenshot = SCREENSHOTS_DIR / f"{timestamp}_{nombre_limpio}.png"

    try:
        driver.save_screenshot(str(ruta_screenshot))
        return ruta_screenshot
    except WebDriverException:
        return None


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Hook de Pytest que guarda screenshot si un test falla.
    Está protegido para no romper Pytest si la sesión del navegador ya no existe.
    """
    resultado = yield
    reporte = resultado.get_result()

    if reporte.when == "call" and reporte.failed:
        driver = item.funcargs.get("driver")

        if not driver:
            return

        ruta_screenshot = guardar_screenshot(driver, item.name)

        if not ruta_screenshot:
            reporte.sections.append(
                ("screenshot", "No se pudo capturar screenshot: sesión del navegador inválida.")
            )
            return

        reporte.sections.append(
            ("screenshot", str(ruta_screenshot))
        )

        try:
            from pytest_html import extras

            extras_reporte = getattr(reporte, "extras", [])
            extras_reporte.append(extras.image(str(ruta_screenshot)))
            reporte.extras = extras_reporte
        except ImportError:
            pass