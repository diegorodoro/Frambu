from django.test import TestCase
from .models import Order

class OrderTestCase(TestCase):
    def test_invalid_client(self):
        # Asumiendo que tienes una función para crear órdenes en tus tests
        response = self.create_order(client_id=9999)  # ID no existente
        self.assertNotEqual(response.status_code, 200)
