from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def crear_driver():
    """Crea y configura una instancia del navegador Chrome."""
    options = Options()
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(5)

    return driver