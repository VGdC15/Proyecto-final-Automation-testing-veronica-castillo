import pytest

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


@pytest.mark.login
def test_login_exitoso_saucedemo(driver, credenciales_validas):
    """Valida que un usuario pueda iniciar sesión correctamente en Sauce Demo."""
    login_page = LoginPage(driver)

    login_page.abrir().realizar_login(
        credenciales_validas["usuario"],
        credenciales_validas["password"],
    )

    inventory_page = InventoryPage(driver).esperar_carga()

    assert inventory_page.esta_en_pagina_inventario()
    assert inventory_page.obtener_titulo() == "Products"


@pytest.mark.login
def test_login_fallido_con_credenciales_invalidas(driver, credenciales_invalidas):
    """Valida que un usuario no pueda iniciar sesión con credenciales inválidas."""
    login_page = LoginPage(driver)

    login_page.abrir().realizar_login(
        credenciales_invalidas["usuario"],
        credenciales_invalidas["password"],
    )

    assert login_page.hay_error_visible()

    mensaje_error = login_page.obtener_mensaje_error()

    assert "Username and password do not match" in mensaje_error
    assert "/inventory.html" not in driver.current_url