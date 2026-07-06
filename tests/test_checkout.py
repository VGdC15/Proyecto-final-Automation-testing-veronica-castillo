import pytest

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


@pytest.mark.checkout
def test_checkout_completo(driver, credenciales_validas, datos_checkout):
    """Valida el flujo completo de compra desde login hasta confirmación final."""
    login_page = LoginPage(driver)

    login_page.abrir().realizar_login(
        credenciales_validas["usuario"],
        credenciales_validas["password"],
    )

    inventory_page = InventoryPage(driver).esperar_carga()

    inventory_page.agregar_primer_producto()

    assert inventory_page.obtener_contador_carrito() == "1"

    cart_page = inventory_page.ir_al_carrito().esperar_carga()

    assert cart_page.esta_en_pagina_carrito()
    assert cart_page.hay_items_en_carrito()

    checkout_page = cart_page.ir_a_checkout().esperar_carga_informacion()

    assert checkout_page.esta_en_pagina_informacion()
    assert checkout_page.obtener_titulo() == "Checkout: Your Information"

    checkout_page.completar_datos_cliente(
        datos_checkout["nombre"],
        datos_checkout["apellido"],
        datos_checkout["codigo_postal"],
    )

    assert checkout_page.obtener_nombre_ingresado() == datos_checkout["nombre"]
    assert checkout_page.obtener_apellido_ingresado() == datos_checkout["apellido"]
    assert checkout_page.obtener_codigo_postal_ingresado() == str(
        datos_checkout["codigo_postal"]
    )

    checkout_page.continuar()

    if checkout_page.hay_error_visible():
        mensaje_error = checkout_page.obtener_mensaje_error()
        raise AssertionError(f"Error visible en checkout: {mensaje_error}")

    checkout_page.esperar_carga_resumen()

    assert checkout_page.esta_en_pagina_resumen()
    assert checkout_page.obtener_titulo() == "Checkout: Overview"
    assert checkout_page.obtener_cantidad_items_resumen() == 1
    assert "Total:" in checkout_page.obtener_total_resumen()

    checkout_page.finalizar_compra()
    checkout_page.esperar_compra_finalizada()

    assert checkout_page.esta_en_pagina_finalizacion()
    assert checkout_page.obtener_titulo() == "Checkout: Complete!"
    assert checkout_page.obtener_mensaje_confirmacion() == "Thank you for your order!"
    assert checkout_page.boton_volver_inicio_visible()