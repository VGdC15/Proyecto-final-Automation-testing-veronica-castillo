from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:
    """Page Object para el flujo de checkout de Sauce Demo."""

    _TITLE = (By.CLASS_NAME, "title")

    _FIRST_NAME_INPUT = (By.ID, "first-name")
    _LAST_NAME_INPUT = (By.ID, "last-name")
    _POSTAL_CODE_INPUT = (By.ID, "postal-code")
    _CONTINUE_BUTTON = (By.ID, "continue")

    _ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")

    _FINISH_BUTTON = (By.ID, "finish")
    _CART_ITEMS = (By.CLASS_NAME, "cart_item")
    _SUMMARY_TOTAL = (By.CLASS_NAME, "summary_total_label")

    _COMPLETE_HEADER = (By.CLASS_NAME, "complete-header")
    _COMPLETE_TEXT = (By.CLASS_NAME, "complete-text")
    _BACK_HOME_BUTTON = (By.ID, "back-to-products")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def esperar_carga_informacion(self):
        """Espera a que cargue la pantalla de información del checkout."""
        self.wait.until(EC.url_contains("/checkout-step-one.html"))
        self.wait.until(EC.visibility_of_element_located(self._TITLE))
        self.wait.until(EC.element_to_be_clickable(self._FIRST_NAME_INPUT))
        self.wait.until(EC.element_to_be_clickable(self._LAST_NAME_INPUT))
        self.wait.until(EC.element_to_be_clickable(self._POSTAL_CODE_INPUT))
        return self

    def esperar_carga_resumen(self):
        """Espera a que cargue la pantalla de resumen del checkout."""
        self.wait.until(EC.url_contains("/checkout-step-two.html"))
        self.wait.until(EC.visibility_of_element_located(self._TITLE))
        self.wait.until(EC.visibility_of_all_elements_located(self._CART_ITEMS))
        return self

    def esperar_compra_finalizada(self):
        """Espera a que cargue la pantalla final del checkout."""
        self.wait.until(EC.url_contains("/checkout-complete.html"))
        self.wait.until(EC.visibility_of_element_located(self._COMPLETE_HEADER))
        return self

    def esta_en_pagina_informacion(self):
        """Indica si estamos en el primer paso del checkout."""
        return "/checkout-step-one.html" in self.driver.current_url

    def esta_en_pagina_resumen(self):
        """Indica si estamos en el resumen del checkout."""
        return "/checkout-step-two.html" in self.driver.current_url

    def esta_en_pagina_finalizacion(self):
        """Indica si estamos en la pantalla final del checkout."""
        return "/checkout-complete.html" in self.driver.current_url

    def obtener_titulo(self):
        """Obtiene el título visible de la página actual del checkout."""
        return self.wait.until(
            EC.visibility_of_element_located(self._TITLE)
        ).text

    def _obtener_campo(self, locator):
        """Obtiene un campo clickeable del formulario."""
        campo = self.wait.until(
            EC.element_to_be_clickable(locator)
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            campo,
        )

        return campo

    def _setear_valor_con_js(self, campo, valor):
        """
        Setea el valor del input usando el setter nativo y dispara eventos.
        Esto ayuda cuando send_keys no actualiza correctamente un input manejado por JS.
        """
        self.driver.execute_script(
            """
            const input = arguments[0];
            const value = arguments[1];

            const nativeInputValueSetter = Object.getOwnPropertyDescriptor(
                window.HTMLInputElement.prototype,
                'value'
            ).set;

            nativeInputValueSetter.call(input, value);

            input.dispatchEvent(new Event('input', { bubbles: true }));
            input.dispatchEvent(new Event('change', { bubbles: true }));
            """,
            campo,
            valor,
        )

    def _escribir_en_campo(self, locator, valor):
        """Escribe un valor en un input de forma robusta."""
        valor = str(valor)

        campo = self._obtener_campo(locator)

        campo.click()
        campo.send_keys(Keys.CONTROL, "a")
        campo.send_keys(Keys.BACKSPACE)
        campo.send_keys(valor)

        valor_actual = campo.get_attribute("value")

        if valor_actual != valor:
            self._setear_valor_con_js(campo, valor)

        self.wait.until(
            lambda _: self._obtener_campo(locator).get_attribute("value") == valor
        )

        return self

    def ingresar_nombre(self, nombre):
        """Completa el campo nombre."""
        return self._escribir_en_campo(self._FIRST_NAME_INPUT, nombre)

    def ingresar_apellido(self, apellido):
        """Completa el campo apellido."""
        return self._escribir_en_campo(self._LAST_NAME_INPUT, apellido)

    def ingresar_codigo_postal(self, codigo_postal):
        """Completa el campo código postal."""
        return self._escribir_en_campo(self._POSTAL_CODE_INPUT, codigo_postal)

    def completar_datos_cliente(self, nombre, apellido, codigo_postal):
        """Completa todos los datos requeridos para continuar el checkout."""
        self.ingresar_nombre(nombre)
        self.ingresar_apellido(apellido)
        self.ingresar_codigo_postal(codigo_postal)
        return self

    def obtener_nombre_ingresado(self):
        """Devuelve el valor cargado en el campo nombre."""
        return self.wait.until(
            EC.visibility_of_element_located(self._FIRST_NAME_INPUT)
        ).get_attribute("value")

    def obtener_apellido_ingresado(self):
        """Devuelve el valor cargado en el campo apellido."""
        return self.wait.until(
            EC.visibility_of_element_located(self._LAST_NAME_INPUT)
        ).get_attribute("value")

    def obtener_codigo_postal_ingresado(self):
        """Devuelve el valor cargado en el campo código postal."""
        return self.wait.until(
            EC.visibility_of_element_located(self._POSTAL_CODE_INPUT)
        ).get_attribute("value")

    def continuar(self):
        """Avanza al resumen del checkout."""
        self.wait.until(
            EC.element_to_be_clickable(self._CONTINUE_BUTTON)
        ).click()
        return self

    def hay_error_visible(self):
        """Indica si hay un mensaje de error visible en el checkout."""
        try:
            return self.wait.until(
                EC.visibility_of_element_located(self._ERROR_MESSAGE)
            ).is_displayed()
        except TimeoutException:
            return False

    def obtener_mensaje_error(self):
        """Devuelve el mensaje de error visible en checkout."""
        return self.wait.until(
            EC.visibility_of_element_located(self._ERROR_MESSAGE)
        ).text

    def finalizar_compra(self):
        """Finaliza la compra."""
        self.wait.until(
            EC.element_to_be_clickable(self._FINISH_BUTTON)
        ).click()
        return self

    def obtener_cantidad_items_resumen(self):
        """Devuelve la cantidad de productos visibles en el resumen."""
        items = self.wait.until(
            EC.visibility_of_all_elements_located(self._CART_ITEMS)
        )
        return len(items)

    def obtener_total_resumen(self):
        """Devuelve el total mostrado en el resumen."""
        return self.wait.until(
            EC.visibility_of_element_located(self._SUMMARY_TOTAL)
        ).text

    def obtener_mensaje_confirmacion(self):
        """Devuelve el mensaje principal de compra finalizada."""
        return self.wait.until(
            EC.visibility_of_element_located(self._COMPLETE_HEADER)
        ).text

    def obtener_texto_confirmacion(self):
        """Devuelve el texto descriptivo de compra finalizada."""
        return self.wait.until(
            EC.visibility_of_element_located(self._COMPLETE_TEXT)
        ).text

    def boton_volver_inicio_visible(self):
        """Indica si el botón para volver al inventario está visible."""
        return self.wait.until(
            EC.visibility_of_element_located(self._BACK_HOME_BUTTON)
        ).is_displayed()