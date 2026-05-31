from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


URL_SAUCEDEMO = "https://www.saucedemo.com"
USUARIO_VALIDO = "standard_user"
PASSWORD_VALIDO = "secret_sauce"


def abrir_login(driver):
    """Abre la página de login de Sauce Demo."""
    driver.get(URL_SAUCEDEMO)


def completar_login(driver, usuario=USUARIO_VALIDO, password=PASSWORD_VALIDO):
    """Completa usuario y contraseña válidos."""
    driver.find_element(By.ID, "user-name").send_keys(usuario)
    driver.find_element(By.ID, "password").send_keys(password)


def hacer_click_login(driver):
    """Hace click en el botón de login."""
    driver.find_element(By.ID, "login-button").click()


def login_exitoso(driver):
    """Realiza el flujo completo de login válido."""
    abrir_login(driver)
    completar_login(driver)
    hacer_click_login(driver)


def validar_url_inventario(driver):
    """Valida que la URL corresponda al inventario."""
    assert "/inventory.html" in driver.current_url


def obtener_titulo_inventario(driver):
    """Devuelve el título visible de la página de inventario."""
    return driver.find_element(
        By.CSS_SELECTOR,
        "div.header_secondary_container .title"
    ).text


def validar_titulo_inventario(driver):
    """Valida que el título del inventario sea Products."""
    titulo = obtener_titulo_inventario(driver)
    assert titulo == "Products"


def obtener_productos(driver):
    """Devuelve la lista de productos visibles."""
    return driver.find_elements(By.CLASS_NAME, "inventory_item")


def validar_productos_visibles(driver):
    """Valida que exista al menos un producto visible."""
    productos = obtener_productos(driver)
    assert len(productos) > 0
    return productos


def validar_elementos_interfaz(driver):
    """Valida elementos importantes de la interfaz: menú, carrito y filtro."""
    menu = driver.find_element(By.ID, "react-burger-menu-btn")
    carrito = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
    filtro = driver.find_element(By.CLASS_NAME, "product_sort_container")

    assert menu.is_displayed()
    assert carrito.is_displayed()
    assert filtro.is_displayed()


def obtener_nombre_producto(producto):
    """Devuelve el nombre visible de un producto."""
    return producto.find_element(By.CLASS_NAME, "inventory_item_name").text


def agregar_producto_al_carrito(producto):
    """Hace click en el botón del producto para agregarlo al carrito."""
    producto.find_element(By.TAG_NAME, "button").click()


def esperar_badge_carrito(driver):
    """Espera explícitamente a que aparezca el contador del carrito."""
    return WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "shopping_cart_badge")
        )
    )


def validar_badge_carrito(driver, cantidad_esperada="1"):
    """Valida que el badge del carrito muestre la cantidad esperada."""
    badge = esperar_badge_carrito(driver)
    assert badge.text == cantidad_esperada


def abrir_carrito(driver):
    """Navega al carrito de compras."""
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()


def obtener_producto_en_carrito(driver):
    """Devuelve el nombre del producto visible en el carrito."""
    producto = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "inventory_item_name")
        )
    )

    return producto.text


def validar_producto_en_carrito(driver, nombre_producto):
    """Valida que el producto agregado esté visible en el carrito."""
    producto_en_carrito = obtener_producto_en_carrito(driver)
    assert producto_en_carrito == nombre_producto