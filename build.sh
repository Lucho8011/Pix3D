#!/usr/bin/env bash
# exit on error
set -o errexit

# Instalar dependencias
pip install -r requirements.txt

# Recolectar archivos estáticos (CSS/JS)
python manage.py collectstatic --no-input

# Migrar la base de datos
python manage.py migrate

python crear_superuser.py