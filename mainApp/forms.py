from django import forms
from .models import Pedido

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = [
            'nombre_cliente', 
            'contacto_cliente', 
            'descripcion_solicitud', 
            'imagen_referencia', 
            'fecha_necesaria'
        ]
        
        widgets = {
            'nombre_cliente': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tu nombre completo'}),
            'contacto_cliente': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Correo o WhatsApp'}),
            'descripcion_solicitud': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Detalles: Talla, color, idea, etc'}),
            'imagen_referencia': forms.FileInput(attrs={'class': 'form-control'}),
            'fecha_necesaria': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
        
        labels = {
            'nombre_cliente': 'Tu Nombre',
            'contacto_cliente': 'Contacto',
            'descripcion_solicitud': '¿Qué necesitas?',
            'imagen_referencia': 'Sube una imagen de ejemplo (Opcional)',
            'fecha_necesaria': '¿Para cuándo lo necesitas?',
        }