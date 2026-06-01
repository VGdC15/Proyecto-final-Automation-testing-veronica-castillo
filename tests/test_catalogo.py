import pytest

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


@pytest.mark.catalogo
def test_catalogo_visible_despues_del_login(driver, credenciales_validas):
    """Valida que el catálogo se muestre correctamente usando Page Object Model."""
    login_page = LoginPage(driver)

    login_page.abrir().realizar_login(
        credenciales_validas["usuario"],
        credenciales_validas["password"],
    )

    inventory_page = InventoryPage(driver)

    assert inventory_page.esta_en_pagina_inventario()
    assert inventory_page.obtener_titulo() == "Products"
    assert inventory_page.hay_productos_visibles()
    assert inventory_page.menu_visible()
    assert inventory_page.filtro_visible()