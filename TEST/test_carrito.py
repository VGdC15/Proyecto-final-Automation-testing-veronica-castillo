from UTILS.driver_factory import crear_driver
from UTILS.saucedemo_helpers import (
    login_exitoso,
    validar_url_inventario,
    validar_productos_visibles,
    obtener_nombre_producto,
    agregar_producto_al_carrito,
    validar_badge_carrito,
    abrir_carrito,
    validar_producto_en_carrito,
)


def test_agregar_producto_al_carrito():
    """Valida que se pueda agregar un producto al carrito y que figure correctamente."""
    driver = crear_driver()

    try:
        login_exitoso(driver)
        validar_url_inventario(driver)

        productos = validar_productos_visibles(driver)
        primer_producto = productos[0]
        nombre_producto = obtener_nombre_producto(primer_producto)

        agregar_producto_al_carrito(primer_producto)
        validar_badge_carrito(driver, "1")

        abrir_carrito(driver)
        validar_producto_en_carrito(driver, nombre_producto)

    finally:
        driver.quit()