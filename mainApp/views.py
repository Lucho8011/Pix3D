from django.shortcuts import render
from .models import Producto

def index(request):
    lista_productos = Producto.objects.all
    data = {
        'productos': lista_productos
    }
    return render(request, 'home.html', data)
