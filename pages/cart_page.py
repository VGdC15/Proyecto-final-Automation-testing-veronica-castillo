from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:
    """Page Object para la página del carrito de Sauce Demo."""

    _TITLE = (By.CLASS_NAME, "title")
    _CART_ITEMS = (By.CLASS_NAME, "cart_item")
    _ITEM_NAMES = (By.CLASS_NAME, "inventory_item_name")
    _ITEM_QUANTITIES = (By.CLASS_NAME, "cart_quantity")
    _CONTINUE_SHOPPING_BUTTON = (By.ID, "continue-shopping")
    _CHECKOUT_BUTTON = (By.ID, "checkout")
    _REMOVE_BUTTONS = (By.CSS_SELECTOR, "button[data-test*='remove']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def esperar_carga(self):
        """Espera a que la página del carrito cargue correctamente."""
        self.wait.until(EC.url_contains("/cart.html"))
        self.wait.until(EC.visibility_of_element_located(self._TITLE))
        return self

    def esta_en_pagina_carrito(self):
        """Indica si la URL actual corresponde al carrito."""
        return "/cart.html" in self.driver.current_url

    def obtener_titulo(self):
        """Obtiene el título visible de la página del carrito."""
        return self.wait.until(
            EC.visibility_of_element_located(self._TITLE)
        ).text

    def obtener_items(self):
        """Obtiene todos los productos visibles en el carrito."""
        return self.wait.until(
            EC.visibility_of_all_elements_located(self._CART_ITEMS)
        )

    def obtener_cantidad_items(self):
        """Devuelve la cantidad de productos agregados al carrito."""
        return len(self.obtener_items())

    def hay_items_en_carrito(self):
        """Indica si el carrito tiene al menos un producto."""
        return self.obtener_cantidad_items() > 0

    def obtener_nombre_primer_item(self):
        """Obtiene el nombre del primer producto del carrito."""
        nombres = self.wait.until(
            EC.visibility_of_all_elements_located(self._ITEM_NAMES)
        )
        return nombres[0].text

    def obtener_cantidad_primer_item(self):
        """Obtiene la cantidad indicada para el primer producto del carrito."""
        cantidades = self.wait.until(
            EC.visibility_of_all_elements_located(self._ITEM_QUANTITIES)
        )
        return cantidades[0].text

    def remover_primer_producto(self):
        """Remueve el primer producto disponible del carrito."""
        botones = self.wait.until(
            EC.visibility_of_all_elements_located(self._REMOVE_BUTTONS)
        )
        botones[0].click()
        return self

    def continuar_comprando(self):
        """Vuelve desde el carrito hacia el inventario."""
        self.wait.until(
            EC.element_to_be_clickable(self._CONTINUE_SHOPPING_BUTTON)
        ).click()

        from pages.inventory_page import InventoryPage
        return InventoryPage(self.driver)

    def ir_a_checkout(self):
        """Navega desde el carrito hacia el checkout."""
        self.wait.until(
            EC.element_to_be_clickable(self._CHECKOUT_BUTTON)
        ).click()

        from pages.checkout_page import CheckoutPage
        return CheckoutPage(self.driver)