# 🛒 Tienda Pix3D - Sistema de Pedidos Personalizados

Bienvenido al repositorio oficial de **Pix3D**, una plataforma web para la gestión de pedidos de productos personalizados (poleras, tazones y figuras 3D).

Este proyecto permite a los clientes explorar un catálogo, solicitar productos personalizados y realizar seguimiento, mientras que los administradores gestionan el ciclo de vida completo del pedido.

---

## 🚀 Funcionalidades Principales

### 👤 Para el Cliente (Frontend)
* **Catálogo Visual:** Vista de productos con buscador y filtros por categoría.
* **Detalle de Producto:** Ficha técnica con descripción ampliada.
* **Solicitud de Pedidos:** Formulario para ingresar datos y subir imágenes de referencia.
* **Tracking en Vivo:** Sistema de seguimiento mediante código único (UUID) para ver el estado del pedido.

### 👮‍♂️ Para el Administrador (Backend)
* **Gestión de Inventario:** Control de productos e insumos.
* **Validaciones de Negocio:** Reglas estrictas para cambios de estado (Ej: No finalizar sin pago).
* **Reportes:** Exportación de pedidos a formato Excel (CSV).
* **Panel Intuitivo:** Filtros avanzados y búsqueda rápida.

---

## 🛠️ Tecnologías Utilizadas

* **Backend:** Python 3.12 + Django 5.2.5
* **Frontend:** HTML5, CSS3, Bootstrap 5.3.0
* **Base de Datos:** SQLite
* **Gestión de Archivos:** Pillow

---

## 📋 Guía de Instalación y Ejecución

Sigue estos pasos para levantar el proyecto en tu entorno local:

### 1. Clonar el repositorio
```bash
git clone [https://github.com/Lucho8011/Pix3D.git](https://github.com/Lucho8011/Pix3D.git)
cd Pix3D
```

### 2. Crear y activar el entorno virtual

-En macOS / Linux:
```bash
python3 -m venv env
source env/bin/activate
```
-En Windows:
```bash
python -m venv env
env\Scripts\activate
```

### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```
### 4. Preparar la Base de Datos
```bash
python3 manage.py migrate
```
### 5. Crear un Superusuario
```bash
python3 manage.py createsuperuser
```
### 6. Iniciar el Servidor
```bash
python3 manage.py runserver