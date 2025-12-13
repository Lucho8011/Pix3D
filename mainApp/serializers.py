from rest_framework import serializers
from .models import Insumo, Pedido

class InsumoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Insumo
        fields = '__all__'