from UTILS.driver_factory import crear_driver
from UTILS.saucedemo_helpers import login_exitoso, validar_url_inventario


def test_login_exitoso_saucedemo():
    """Valida que un usuario pueda iniciar sesión correctamente en Sauce Demo."""
    driver = crear_driver()

    try:
        login_exitoso(driver)
        validar_url_inventario(driver)

    finally:
        driver.quit()