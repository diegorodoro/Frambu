from django.db import models
from products.models import Product
from clients.models import Client

class Order(models.Model):
    STATE_CHOICES = [
        ('unpaid', 'Unpaid'),
        ('paid', 'Paid'),
        ('cooking', 'Cooking'),
        ('packaging', 'Packaging'),
        ('labelling', 'Labelling'),
        ('ready', 'Ready')
    ]
    FLAVOUR_CHOICES = [
        ('frambuesa', 'Frambuesa'),
        ('zarzamora', 'Zarzamora'),
        ('fresa', 'Fresa'),
        ('mango', 'Mango'),
        ('mora azul', 'Mora azul'),
    ]

    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='orders')
    product = models.CharField(max_length=20, choices=FLAVOUR_CHOICES, default='frambuesa')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    quantityRequested = models.IntegerField()
    is_paid = models.BooleanField(default=False)
    order_state = models.CharField(max_length=20, choices=STATE_CHOICES, default='unpaid')

    def _str_(self):
        return str(self.id)

    def has_sufficient_stock(self):
        for product in self.products.all():
            if product.stock - self.quantity_requested < 0:
                return False
        return True

