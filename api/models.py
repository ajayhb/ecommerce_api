from django.db import models


class Product(models.Model):
    """Model representing a product in the e-commerce platform."""
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.FloatField()
    stock = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Order(models.Model):
    """Model representing an order containing multiple products."""
    STATUS_CHOICES = [('pending', 'Pending'), ('completed', 'Completed')]

    products = models.JSONField()
    total_price = models.FloatField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')

    def save(self, *args, **kwargs):
        """Override save method to handle stock validation before order is placed."""
        for item in self.products:
            try:
                product = Product.objects.get(id=item["product_id"])
                if product.stock < item["quantity"]:
                    raise ValueError(f"Insufficient stock for {product.name}")
                product.stock -= item["quantity"]
                product.save()
            except Product.DoesNotExist:
                raise ValueError(f"Product with ID {item['product_id']} does not exist.")
        super().save(*args, **kwargs)
