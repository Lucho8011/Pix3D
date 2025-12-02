from django.contrib import admin
from django .utils.html import format_html
from .models import Categoria, Insumo, Producto, Pedido
import csv
from django.http import HttpResponse

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id_categoria', 'nombre_categoria')
    search_fields = ('nombre_categoria',)

@admin.register(Insumo)
class InsumoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'tipo', 'cantidad', 'unidad', 'marca', 'color')
    search_fields = ('tipo', 'marca','nombre',)
    list_filter = ('tipo',)
    list_editable = ('cantidad',)

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria', 'precio_base', 'destacado', 'ver_imagen')
    search_fields = ('nombre', 'descripcion')
    list_filter = ('categoria', 'destacado',)
    list_editable = ('precio_base','destacado',)

    def ver_imagen(self, obj):
        if obj.imagen_1:
            return format_html('<img src="{}" width="50" height="50" />', obj.imagen_1.url)
        return "sin imagen"
    ver_imagen.short_description = 'Vista previa'

def exportar_csv(modeladmin, request,queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="reporte_pedidos.csv"'
    
    writer = csv.writer(response)
    writer.writerow(['ID', 'Nombre Cliente', 'Producto ', 'Estado', 'Estado Pago', 'Fecha Solicitud', 'Total'])
    for pedido in queryset:
        writer.writerow([
            pedido.id, 
            pedido.nombre_cliente, 
            pedido.producto_referencia.nombre if pedido.producto_referencia else 'Sin producto', 
            pedido.fecha_solicitud, 
            pedido.get_estado_display(), 
            pedido.get_estado_pago_display(), 
            pedido.producto_referencia.precio_base if pedido.producto_referencia else 0
            ])
    return response
exportar_csv.short_description = "Exportar pedidos seleccionados a CSV"

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre_cliente', 'plataforma', 'estado', 'estado_pago', 'fecha_solicitud')
    search_fields = ('nombre_cliente', 'contacto_cliente','token_seguimiento',)
    list_filter = ('plataforma', 'estado', 'estado_pago', 'fecha_solicitud',)
    date_hierarchy = 'fecha_solicitud'
    actions = [exportar_csv]

    fieldsets = (
        ('Datos del Cliente', {
            'fields': ('nombre_cliente', 'contacto_cliente')
        }),
        ('Detalles del Pedido', {
            'fields': ('producto_referencia', 'descripcion_solicitud', 'imagen_referencia', 'fecha_necesaria')
        }),
        ('Gestion Interna', {
            'fields': ('plataforma','estado', 'estado_pago',)
        }),
    )

    readonly_fields = ('token_seguimiento',)