import os
import django

# 1. Configurar el entorno de Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Pix3D.settings")
django.setup()

from django.contrib.auth.models import User

# 2. Crear el superusuario si no existe
def crear_admin():
    username = 'admin'
    password = 'admin'
    email = 'admin@example.cl'

    if not User.objects.filter(username=username).exists():
        print(f"Creando superusuario: {username}...")
        User.objects.create_superuser(username, email, password)
        print("✅ ¡Superusuario creado exitosamente!")
    else:
        print("ℹ️ El usuario admin ya existe. No es necesario crearlo.")

if __name__ == "__main__":
    crear_admin()