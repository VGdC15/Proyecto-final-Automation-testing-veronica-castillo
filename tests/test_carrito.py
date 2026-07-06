import pytest

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


@pytest.mark.carrito
def test_agregar_producto_al_carrito(driver, credenciales_validas):
    """Valida que un producto pueda agregarse correctamente al carrito."""
    login_page = LoginPage(driver)

    login_page.abrir().realizar_login(
        credenciales_validas["usuario"],
        credenciales_validas["password"],
    )

    inventory_page = InventoryPage(driver).esperar_carga()

    nombre_producto = inventory_page.obtener_nombre_primer_producto()

    inventory_page.agregar_primer_producto()

    assert inventory_page.obtener_contador_carrito() == "1"

    cart_page = inventory_page.ir_al_carrito().esperar_carga()

    assert cart_page.esta_en_pagina_carrito()
    assert cart_page.obtener_titulo() == "Your Cart"
    assert cart_page.hay_items_en_carrito()
    assert cart_page.obtener_cantidad_items() == 1
    assert cart_page.obtener_nombre_primer_item() == nombre_producto
    assert cart_page.obtener_cantidad_primer_item() == "1"