import pytest

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


@pytest.mark.smoke
@pytest.mark.carrito
def test_agregar_producto_al_carrito(driver, credenciales_validas):
    """Valida agregar un producto al carrito usando Page Object Model."""
    login_page = LoginPage(driver)

    login_page.abrir().realizar_login(
        credenciales_validas["usuario"],
        credenciales_validas["password"],
    )

    inventory_page = InventoryPage(driver)

    assert inventory_page.esta_en_pagina_inventario()

    nombre_producto = inventory_page.obtener_nombre_primer_producto()

    inventory_page.agregar_primer_producto()

    assert inventory_page.obtener_contador_carrito() == "1"

    cart_page = inventory_page.ir_al_carrito()

    assert cart_page.esta_en_pagina_carrito()
    assert cart_page.obtener_cantidad_productos() == 1
    assert cart_page.contiene_producto(nombre_producto)