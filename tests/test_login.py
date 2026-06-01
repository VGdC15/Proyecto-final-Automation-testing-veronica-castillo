import pytest

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


@pytest.mark.smoke
@pytest.mark.login
def test_login_exitoso_saucedemo(driver, credenciales_validas):
    """Valida login exitoso usando Page Object Model."""
    login_page = LoginPage(driver)

    login_page.abrir().realizar_login(
        credenciales_validas["usuario"],
        credenciales_validas["password"],
    )

    inventory_page = InventoryPage(driver)

    assert inventory_page.esta_en_pagina_inventario()
    assert inventory_page.obtener_titulo() == "Products"