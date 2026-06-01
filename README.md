# 🧪 Pre-Entrega Automation Testing - Verónica Castillo

## 📌 Descripción del Proyecto

Este proyecto corresponde a la pre-entrega del curso de Automation Testing.

El objetivo es automatizar flujos básicos de navegación utilizando **Python**, **Pytest** y **Selenium WebDriver** sobre el sitio de práctica:

https://www.saucedemo.com

Las pruebas implementadas permiten validar funcionalidades fundamentales de una aplicación web, incluyendo:

* Inicio de sesión con credenciales válidas.
* Navegación hacia el catálogo de productos.
* Verificación de elementos importantes de la interfaz.
* Agregado de productos al carrito de compras.
* Validación del contenido del carrito.

---

## 🚀 Tecnologías Utilizadas

* Python 3
* Selenium WebDriver
* Pytest
* Google Chrome
* ChromeDriver
* Git
* GitHub

---

## 📁 Estructura del Proyecto

```text
pre-entrega-automation-testing-veronica-castillo/
│
├── TEST/
│   ├── test_login.py
│   ├── test_catalogo.py
│   └── test_carrito.py
│
├── UTILS/
│   ├── driver_factory.py
│   └── saucedemo_helpers.py
│
├── reports/
│
├── .gitignore
└── README.md
```

---

## ⚙️ Instalación de Dependencias

### Clonar el repositorio

```bash
git clone https://github.com/VGdC15/pre-entrega-automation-testing-veronica-castillo.git
```

### Ingresar al proyecto

```bash
cd pre-entrega-automation-testing-veronica-castillo
```

### Instalar Selenium

```bash
pip install selenium
```

### Instalar Pytest

```bash
pip install pytest
```

### Instalar Pytest HTML

```bash
pip install pytest-html
```

---

## ▶️ Ejecución de Pruebas

### Ejecutar todos los tests

```bash
python -m pytest TEST -v
```

### Ejecutar únicamente el test de Login

```bash
python -m pytest TEST/test_login.py -v
```

### Ejecutar únicamente el test de Catálogo

```bash
python -m pytest TEST/test_catalogo.py -v
```

### Ejecutar únicamente el test de Carrito

```bash
python -m pytest TEST/test_carrito.py -v
```

---

## 📊 Generación de Reporte HTML

Para generar un reporte HTML con los resultados de ejecución:

```bash
python -m pytest TEST -v --html=reports/reporte.html
```

Al finalizar, el archivo se encontrará en:

```text
reports/reporte.html
```

y podrá abrirse desde cualquier navegador.

---

## ✅ Casos de Prueba Implementados

### Login

* Navegar a Sauce Demo.
* Ingresar usuario y contraseña válidos.
* Verificar redirección al inventario.

### Catálogo

* Verificar título de la página.
* Validar presencia de productos visibles.
* Validar elementos principales de la interfaz.

### Carrito

* Agregar producto al carrito.
* Verificar contador del carrito.
* Acceder al carrito.
* Validar que el producto agregado esté presente.

### Reporte HTML
<img width="854" height="515" alt="image" src="https://github.com/user-attachments/assets/613a4243-6b68-4a91-bec9-8d03ff47a991" />

---

## 👩‍💻 Autor

**Verónica Castillo**

Pre-Entrega - Automation Testing
Buenos Aires Aprende / Talento Tech
