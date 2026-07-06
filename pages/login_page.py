from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    """Page Object para la página de login de Sauce Demo."""

    URL = "https://www.saucedemo.com/"

    _USER_INPUT = (By.ID, "user-name")
    _PASSWORD_INPUT = (By.ID, "password")
    _LOGIN_BUTTON = (By.ID, "login-button")
    _ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def abrir(self):
        """Abre la página de login."""
        self.driver.get(self.URL)
        return self

    def ingresar_usuario(self, usuario):
        """Ingresa el usuario."""
        campo_usuario = self.wait.until(
            EC.visibility_of_element_located(self._USER_INPUT)
        )
        campo_usuario.clear()
        campo_usuario.send_keys(usuario)
        return self

    def ingresar_password(self, password):
        """Ingresa la contraseña."""
        campo_password = self.wait.until(
            EC.visibility_of_element_located(self._PASSWORD_INPUT)
        )
        campo_password.clear()
        campo_password.send_keys(password)
        return self

    def hacer_click_login(self):
        """Hace click en el botón de login."""
        self.wait.until(
            EC.element_to_be_clickable(self._LOGIN_BUTTON)
        ).click()
        return self

    def realizar_login(self, usuario, password):
        """Realiza el flujo completo de login."""
        self.ingresar_usuario(usuario)
        self.ingresar_password(password)
        self.hacer_click_login()
        return self

    def obtener_mensaje_error(self):
        """Devuelve el mensaje de error visible."""
        return self.wait.until(
            EC.visibility_of_element_located(self._ERROR_MESSAGE)
        ).text

    def hay_error_visible(self):
        """Indica si el mensaje de error está visible."""
        try:
            return self.wait.until(
                EC.visibility_of_element_located(self._ERROR_MESSAGE)
            ).is_displayed()
        except TimeoutException:
            return False