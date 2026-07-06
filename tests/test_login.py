from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from UTILS.driver_factory import crear_driver
from pages.login_page import LoginPage


def test_login_exitoso_saucedemo():
    """Valida que un usuario pueda iniciar sesión correctamente en Sauce Demo."""
    driver = crear_driver()

    try:
        login_page = LoginPage(driver)

        login_page.abrir()
        login_page.realizar_login("standard_user", "secret_sauce")

        WebDriverWait(driver, 10).until(
            EC.url_contains("/inventory.html")
        )

        assert "/inventory.html" in driver.current_url

    finally:
        driver.quit()