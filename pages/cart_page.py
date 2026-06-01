from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:
    """Page Object para la página del carrito de Sauce Demo."""

    _CART_ITEMS = (By.CLASS_NAME, "cart_item")
    _ITEM_NAMES = (By.CLASS_NAME, "inventory_item_name")
    _CONTINUE_SHOPPING_BUTTON = (By.ID, "continue-shopping")
    _CHECKOUT_BUTTON = (By.ID, "checkout")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.wait.until(EC.url_contains("cart.html"))

    def esta_en_pagina_carrito(self):
        """Valida que la URL actual corresponda al carrito."""
        return "/cart.html" in self.driver.current_url

    def obtener_productos_en_carrito(self):
        """Obtiene todos los productos visibles en el carrito."""
        return self.wait.until(
            EC.visibility_of_all_elements_located(self._CART_ITEMS)
        )

    def obtener_cantidad_productos(self):
        """Devuelve la cantidad de productos visibles en el carrito."""
        return len(self.obtener_productos_en_carrito())

    def obtener_nombres_productos(self):
        """Obtiene los nombres de los productos del carrito."""
        productos = self.wait.until(
            EC.visibility_of_all_elements_located(self._ITEM_NAMES)
        )
        return [producto.text for producto in productos]

    def contiene_producto(self, nombre_producto):
        """Indica si el carrito contiene un producto por nombre."""
        return nombre_producto in self.obtener_nombres_productos()

    def continuar_comprando(self):
        """Vuelve a la página de inventario."""
        self.wait.until(
            EC.element_to_be_clickable(self._CONTINUE_SHOPPING_BUTTON)
        ).click()

        from pages.inventory_page import InventoryPage
        return InventoryPage(self.driver)

    def checkout_visible(self):
        """Indica si el botón de checkout está visible."""
        return self.wait.until(
            EC.visibility_of_element_located(self._CHECKOUT_BUTTON)
        ).is_displayed()