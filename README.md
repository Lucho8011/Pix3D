# 🛒 Tienda Pix3D - Sistema de Pedidos & API REST

**Despliegue en Nube y Arquitectura de Servicios**

Bienvenido al repositorio de **Pix3D**, una plataforma web desplegada en la nube para la gestión de pedidos personalizados. Este proyecto evoluciona la versión anterior integrando **Base de Datos PostgreSQL**, **APIs RESTful** y un **Dashboard del Negocio**.

## 🚀 Enlaces del Proyecto (Deploy)
* 🌐 **Sitio Web (Render):** [https://tienda-pix3d-eval4.onrender.com/](hhttps://tienda-pix3d-eval4.onrender.com/)
---

## 🌟 Nuevas Funcionalidades (Versión Cloud)

### 📊 Business Intelligence (Dashboard)
* **Reportes Gráficos:** Implementación de **Chart.js** para visualizar el estado de pedidos y métricas de ventas en tiempo real (`/reporte/`).
* **Datos Dinámicos:** Los gráficos se alimentan directamente de la base de datos PostgreSQL.

### 🔌 API REST (Django REST Framework)
El sistema expone endpoints para integración con otros sistemas:
1.  **Insumos (CRUD Completo):** `/api/insumos/`
2.  **Pedidos (Seguridad):** `/api/pedidos/` 
3.  **Filtros Avanzados:** `/api/pedidos/filtrar/?estado=SOL` 

### ☁️ Infraestructura Cloud (Render)
* **Base de Datos Híbrida:** SQLite para desarrollo local y **PostgreSQL** para producción.
* **Archivos Estáticos:** Gestión optimizada con **WhiteNoise**.
* **Automatización:** Script `build.sh` y creación automática de superusuario.

---

## 🛠️ Tecnologías Utilizadas

* **Backend:** Python 3.12, Django 5.2, **Django REST Framework**.
* **Frontend:** HTML5, Bootstrap 5, **Chart.js**.
* **Servidor:** Gunicorn + WhiteNoise.
* **Base de Datos:**
    * 🔴 Local: SQLite
    * 🟢 Producción: **PostgreSQL** (Render).
* **Despliegue:** Render.com

---

## 📋 Guía de Instalación Local 

Si deseas correr este proyecto en tu máquina local (Windows/Mac) en lugar de ver la versión nube:

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
```Bash
python -m venv env
env\Scripts\activate
```
### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```
### 4. Preparar la Base de Datos
```Bash
python3 manage.py migrate
```
### 5. Crear un Superusuario
```Bash
python3 manage.py createsuperuser
```
### 6. Iniciar el Servidor
```Bash
python3 manage.py runserver
```