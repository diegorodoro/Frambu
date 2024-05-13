from django import forms
from .models import Order
from clients.models import Client

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['client', 'product', 'quantityRequested', 'is_paid']

    def clean_client(self):
        client = self.cleaned_data.get('client')
        if not Client.objects.filter(id=client.id).exists():
            raise forms.ValidationError("Cliente no válido.")
        return client
