from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto, Pedido, Categoria, Insumo
from .forms import PedidoForm
from .serializers import InsumoSerializer
from .serializers import PedidoSerializer
from rest_framework import viewsets, mixins
from rest_framework.views import APIView
from rest_framework.response import Response
from datetime import datetime
from django.db.models import Count
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils.dateparse import parse_date
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

#api 1 - Insumo
class InsumoViewSet(viewsets.ModelViewSet):
    queryset = Insumo.objects.all()
    serializer_class = InsumoSerializer
#api 2 - crear y modifcar pedido
class PedidoViewSet(mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    viewsets.GenericViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer
# api 3 - filtro
class PedidoFilterView(APIView):
    def get(self, request):
        fecha_inicio = request.query_params.get('fecha_inicio')
        fecha_fin = request.query_params.get('fecha_fin')
        estado = request.query_params.get('estado')
        limite = request.query_params.get('limite')

        pedidos = Pedido.objects.all()

        if fecha_inicio and fecha_fin:
            pedidos = pedidos.filter(fecha_solicitud__range=[fecha_inicio, fecha_fin])

        if estado:
            pedidos = pedidos.filter(estado=estado)
        
        if limite:
            try:
                pedidos = pedidos[:int(limite)]
            except ValueError:
                pass
        
        serializer = PedidoSerializer(pedidos, many=True)
        return Response(serializer.data)

# Vista reporte
@login_required
def reporte_pedidos(request):
    pedidos = Pedido.objects.all()
    fecha_inicio = request.GET.get('fecha_inicio')
    fecha_fin = request.GET.get('fecha_fin')
    if fecha_inicio and fecha_fin:
        pedidos = pedidos.filter(fecha_solicitud__range=[fecha_inicio, fecha_fin])

    #Agrupaciones(graficos)
    #pedidos por estado(grafico de torta)
    data_estados = pedidos.values('estado').annotate(total=Count('id'))

    #pedidos por plataforma(grafico de barras)
    data_plataforma = pedidos.values('plataforma').annotate(total=Count('id'))

    #Listas
    labels_estados = [item['estado'] for item in data_estados]
    counts_estados = [item['total'] for item in data_estados]
    labels_plat = [item['plataforma'] for item in data_plataforma if item['plataforma']]
    counts = [item['total'] for item in data_plataforma if item['plataforma']]
    context = {
        'pedidos': pedidos,
        'labels_estados': labels_estados,
        'counts_estados': counts_estados,
        'labels_plat': labels_plat,
        'counts': counts,
    }
    return render(request, 'reporte.html', context)