from selenium.webdriver.common.by import By
from UTILS.driver_factory import crear_driver


def test_catalogo_visible_despues_del_login():
    """Valida que el catálogo de productos se muestre correctamente después del login."""

    driver = crear_driver()

    try:
        # 1. Navego a la página de login
        driver.get("https://www.saucedemo.com")

        # 2. Ingreso credenciales válidas
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")

        # 3. Click en el botón de login
        driver.find_element(By.ID, "login-button").click()

        # 4. Valido redirección al inventario
        assert "/inventory.html" in driver.current_url

        # 5. Verifico que el título de la página de inventario sea correcto
        titulo = driver.find_element(
            By.CSS_SELECTOR,
            "div.header_secondary_container .title"
        ).text

        assert titulo == "Products"

        # 6. Verifico que exista al menos un producto visible
        productos = driver.find_elements(By.CLASS_NAME, "inventory_item")

        assert len(productos) > 0

        # 7. Valido elementos importantes de la interfaz
        menu = driver.find_element(By.ID, "react-burger-menu-btn")
        carrito = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
        filtro = driver.find_element(By.CLASS_NAME, "product_sort_container")

        assert menu.is_displayed()
        assert carrito.is_displayed()
        assert filtro.is_displayed()

    finally:
        driver.quit()