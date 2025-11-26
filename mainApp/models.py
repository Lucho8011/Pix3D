from django.db import models
import uuid #generacion de token unico

#Para organizacion de productos
class Categoria(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    nombre_categoria = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_categoria

#Para inventario de insumos internos
class Insumo(models.Model):
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)
    cantidad = models.IntegerField(default=0)
    unidad = models.CharField(max_length=100, blank=True, null=True)
    marca = models.CharField(max_length=100, blank=True, null=True)
    color = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} - ({self.cantidad})"
    

class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    precio_base = models.IntegerField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    imagen_1 = models.ImageField(upload_to='productos/', blank=True, null=True)
    imagen_2 = models.ImageField(upload_to='productos/', blank=True, null=True)
    imagen_3 = models.ImageField(upload_to='productos/', blank=True, null=True)
    destacado = models.BooleanField(default=False)
    def __str__(self):
        return self.nombre
    
class Pedido(models.Model):
    PLATAFORMAS = [
        ('FB', 'Facebook'),
        ('IG', 'Instagram'),
        ('WA', 'Whatsapp'),
        ('PR', 'Presencial'),
        ('WEB', 'Sitio Web'),
        ('OT', 'Otro'),
    ]
    ESTADOS_PEDIDOS = [
        ('SOL', 'Solicitado'),
        ('APR', 'Aprobado'),
        ('PRO', 'En Proceso'),
        ('REA', 'Realizada'),
        ('ENT', 'Entregada'),
        ('FIN', 'Finalizada'),
        ('CAN', 'Cancelada'),
    ]   

    ESTADOS_PAGO = [
        ('PEN', 'Pendiente'),
        ('PAR', 'Parcial'),
        ('PAG', 'Pagado'),
    ]

#Datos del cliente
    nombre_cliente = models.CharField(max_length=100)
    contacto_cliente = models.CharField(max_length=100, help_text="Número de teléfono o correo electrónico")

#Datos del pedido
    producto_referencia = models.ForeignKey(Producto, on_delete=models.CASCADE)
    descripcion_solicitud = models.TextField()
    imagen_referencia = models.ImageField(upload_to='pedidos_refs/', blank=True, null=True)
    fecha_solicitud = models.DateTimeField(auto_now_add=True)
    fecha_necesaria = models.DateField(null=True, blank=True)

#datos de gestion interna
    plataforma = models.CharField(max_length=3, choices=PLATAFORMAS,default='WEB')
    estado = models.CharField(max_length=3, choices=ESTADOS_PEDIDOS, default='SOL')
    estado_pago = models.CharField(max_length=3, choices=ESTADOS_PAGO, default='PEN')

    #Token unico para seguimiento(UUID)
    token_seguimiento = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    def __str__(self):
        return f"Pedido {self.id} - {self.nombre_cliente}"