import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


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

    navegador.quit()


@pytest.fixture
def credenciales_validas():
    return {
        "usuario": "standard_user",
        "password": "secret_sauce",
    }


@pytest.fixture
def credenciales_invalidas():
    return {
        "usuario": "usuario_invalido",
        "password": "clave_invalida",
    }


@pytest.fixture
def usuario_bloqueado():
    return {
        "usuario": "locked_out_user",
        "password": "secret_sauce",
    }

@pytest.fixture
def datos_checkout():
    return {
        "nombre": "Veronica",
        "apellido": "Castillo",
        "codigo_postal": "1824",
    }