from rest_framework import serializers
from .models import Order

class OrderSerializers(serializers.ModelSerializer):
    class Meta:
        model = Order
        # excluye todos los campos excepto 'id' y 'is_paid'
        # exclude = ('products', 'created_at', 'updated_at', 'quantityRequested', 'order_state')
        fields = ['id']


class OrderSerializers2(serializers.ModelSerializer):
    class Meta:
        model = Order
        # excluye todos los campos excepto 'id' y 'is_paid'
        exclude = ('products', 'created_at', 'updated_at', 'quantityRequested')