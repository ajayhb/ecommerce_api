from django.test import TestCase
from .models import Product, Order
from rest_framework import status 
from rest_framework.test import APIClient


class ProductTestCase(TestCase):
    def setUp(self):
        Product.objects.create(name="Laptop", description="Gaming Laptop", price=1000, stock=10)

    def test_create_product(self):
        product = Product.objects.get(name="Laptop")
        self.assertEqual(product.stock, 10)

class OrderTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.product = Product.objects.create(name="Phone", description="Smartphone", price=500, stock=3)

    def test_create_order_positive(self):
        _ = Order.objects.create(products=[{"product_id": self.product.id, "quantity": 2}], total_price=1000)
        self.product.refresh_from_db()
        self.assertEqual(self.product.stock, 1)

    def test_create_order_negative(self):
        response = self.client.post(
            "/orders/",
            {  
                # Exceeding stock
                "products": [{"product_id": self.product.id, "quantity": 4}],
                "total_price": 1000,
                "status": "pending"
            },
            format="json"
        )

        # Ensure a 400 error is returned
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data["error"], "Insufficient stock for Phone")

        # Ensure stock remains unchanged
        self.product.refresh_from_db()
        self.assertEqual(self.product.stock, 3)  # Stock should not be deducted

from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Product


class ProductTestCase(TestCase):
    """Test case for Product model."""

    def setUp(self):
        self.client = APIClient()
        self.product = Product.objects.create(name="Laptop", description="Gaming Laptop", price=1000, stock=10)

    def test_create_product(self):
        """Test if product is created successfully."""
        self.assertEqual(self.product.stock, 10)


class OrderTestCase(TestCase):
    """Test case for Order model & order placement."""

    def setUp(self):
        self.client = APIClient()
        self.product = Product.objects.create(name="Phone", description="Smartphone", price=500, stock=3)

    def test_create_order_positive(self):
        _ = Order.objects.create(products=[{"product_id": self.product.id, "quantity": 2}], total_price=1000)
        self.product.refresh_from_db()
        self.assertEqual(self.product.stock, 1)

    def test_create_order_negative(self):
        """Test if placing an order with insufficient stock returns 400 error."""
        response = self.client.post(
            "/orders/",
            {
                "products": [{"product_id": self.product.id, "quantity": 4}],  # Exceeding stock
                "total_price": 1000,
                "status": "pending"
            },
            format="json"
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("error", response.data)
        self.assertEqual(response.data["error"], "Insufficient stock for Phone")

        # Ensure stock remains unchanged
        self.product.refresh_from_db()
        self.assertEqual(self.product.stock, 3)
