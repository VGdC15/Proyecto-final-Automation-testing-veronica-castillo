from UTILS.driver_factory import crear_driver
from UTILS.saucedemo_helpers import (
    login_exitoso,
    validar_url_inventario,
    validar_titulo_inventario,
    validar_productos_visibles,
    validar_elementos_interfaz,
)


def test_catalogo_visible_despues_del_login():
    """Valida que el catálogo de productos se muestre correctamente después del login."""
    driver = crear_driver()

    try:
        login_exitoso(driver)
        validar_url_inventario(driver)
        validar_titulo_inventario(driver)
        validar_productos_visibles(driver)
        validar_elementos_interfaz(driver)

    finally:
        driver.quit()