from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto, Pedido, Categoria
from .forms import PedidoForm

#vita de la portada
def index(request):
    productos = Producto.objects.all()
    categorias = Categoria.objects.all()

    # Buscador
    busqueda = request.GET.get('buscar')
    if busqueda:
        productos = productos.filter(nombre__icontains=busqueda)
    
    # Filtro por Categoría
    categoria_id = request.GET.get('categoria')
    if categoria_id:
        productos = productos.filter(categoria_id=categoria_id)
            
    data = {
        'productos': productos,
        'categorias': categorias,
    }
    return render(request, 'home.html', data)

# Vista pedido
def realizar_pedido(request, pk):
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
    
#Vista Tracking
def seguimiento(request, token):
    pedido = get_object_or_404(Pedido, token_seguimiento=token)
    return render(request, 'seguimiento.html', {'pedido': pedido})

#Vista detalle
def detalle(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    return render(request, 'detalle.html', {'producto': producto})