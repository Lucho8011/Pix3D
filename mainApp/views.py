from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto, Pedido
from .forms import PedidoForm

def index(request):
    lista_productos = Producto.objects.all()
    data = {
        'productos': lista_productos
    }
    return render(request, 'home.html', data)

def realizar_pedido(request,pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        formulario = PedidoForm(request.POST, request.FILES)
        if formulario.is_valid():
            pedido = formulario.save(commit=False)
            pedido.producto_referencia = producto
            pedido.plataforma = 'Web'
            pedido.save()
            return render(request, 'solicitud.html', {'pedido': pedido})
    else:
        formulario = PedidoForm()
        return render(request, 'formulario.html', {'form': formulario, 'producto': producto})
    
def seguimiento(request, token):
    pedido = get_object_or_404(Pedido, token_seguimiento=token)
    return render(request, 'seguimiento.html', {'pedido': pedido})
