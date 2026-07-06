from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InventoryPage:
    """Page Object para la página de inventario de Sauce Demo."""

    _TITLE = (By.CLASS_NAME, "title")
    _PRODUCTS = (By.CLASS_NAME, "inventory_item")
    _PRODUCT_NAMES = (By.CLASS_NAME, "inventory_item_name")
    _ADD_BUTTONS = (By.CSS_SELECTOR, "button[data-test*='add-to-cart']")
    _CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    _CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    _MENU_BUTTON = (By.ID, "react-burger-menu-btn")
    _SORT_SELECT = (By.CLASS_NAME, "product_sort_container")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def esperar_carga(self):
        """Espera a que la página de inventario cargue correctamente."""
        self.wait.until(EC.url_contains("/inventory.html"))
        self.wait.until(EC.visibility_of_element_located(self._TITLE))
        self.wait.until(EC.visibility_of_all_elements_located(self._PRODUCTS))
        return self

    def esta_en_pagina_inventario(self):
        """Indica si la URL actual corresponde al inventario."""
        return "/inventory.html" in self.driver.current_url

    def obtener_titulo(self):
        """Obtiene el título visible del inventario."""
        return self.wait.until(
            EC.visibility_of_element_located(self._TITLE)
        ).text

    def obtener_productos(self):
        """Obtiene todos los productos visibles."""
        return self.wait.until(
            EC.visibility_of_all_elements_located(self._PRODUCTS)
        )

    def obtener_cantidad_productos(self):
        """Devuelve la cantidad de productos visibles."""
        return len(self.obtener_productos())

    def hay_productos_visibles(self):
        """Indica si existe al menos un producto visible."""
        return self.obtener_cantidad_productos() > 0

    def obtener_nombre_primer_producto(self):
        """Obtiene el nombre del primer producto visible."""
        nombres = self.wait.until(
            EC.visibility_of_all_elements_located(self._PRODUCT_NAMES)
        )
        return nombres[0].text

    def agregar_primer_producto(self):
        """Agrega el primer producto disponible al carrito."""
        botones = self.wait.until(
            EC.visibility_of_all_elements_located(self._ADD_BUTTONS)
        )
        botones[0].click()
        return self

    def obtener_contador_carrito(self):
        """Obtiene el número que aparece en el badge del carrito."""
        badge = self.wait.until(
            EC.visibility_of_element_located(self._CART_BADGE)
        )
        return badge.text

    def ir_al_carrito(self):
        """Navega hacia la página del carrito."""
        self.wait.until(
            EC.element_to_be_clickable(self._CART_LINK)
        ).click()

        from pages.cart_page import CartPage
        return CartPage(self.driver)

    def menu_visible(self):
        """Indica si el botón de menú está visible."""
        return self.wait.until(
            EC.visibility_of_element_located(self._MENU_BUTTON)
        ).is_displayed()

    def carrito_visible(self):
        """Indica si el enlace del carrito está visible."""
        return self.wait.until(
            EC.visibility_of_element_located(self._CART_LINK)
        ).is_displayed()

    def filtro_visible(self):
        """Indica si el filtro de productos está visible."""
        return self.wait.until(
            EC.visibility_of_element_located(self._SORT_SELECT)
        ).is_displayed()