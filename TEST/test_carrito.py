from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from UTILS.driver_factory import crear_driver


def test_agregar_producto_al_carrito():
    """Valida que se pueda agregar un producto al carrito y que figure correctamente."""

    driver = crear_driver()

    try:
        # 1. Navego a Sauce Demo
        driver.get("https://www.saucedemo.com")

        # 2. Login con credenciales válidas
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        # 3. Valido que estamos en inventario
        assert "/inventory.html" in driver.current_url

        # 4. Obtengo el primer producto
        primer_producto = driver.find_elements(By.CLASS_NAME, "inventory_item")[0]

        nombre_producto = primer_producto.find_element(
            By.CLASS_NAME,
            "inventory_item_name"
        ).text

        # 5. Añado el producto al carrito
        primer_producto.find_element(By.TAG_NAME, "button").click()

        # 6. Verifico que el contador del carrito se incremente correctamente
        badge_carrito = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                (By.CLASS_NAME, "shopping_cart_badge")
            )
        )

        assert badge_carrito.text == "1"

        # 7. Navego al carrito de compras
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

        # 8. Compruebo que el producto añadido aparezca correctamente
        producto_en_carrito = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                (By.CLASS_NAME, "inventory_item_name")
            )
        )

        assert producto_en_carrito.text == nombre_producto

    finally:
        driver.quit()