from rest_framework import serializers
from .models import Product, Order


class ProductSerializer(serializers.ModelSerializer):
    """Serializer for Product model."""

    class Meta:
        model = Product
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    """Serializer for Order model."""
    products = serializers.JSONField()

    class Meta:
        model = Order
        fields = '__all__'

    def validate_products(self, value):
        """Validate that products list is well-formed."""
        if not isinstance(value, list):
            raise serializers.ValidationError("Products must be a list of {product_id, quantity}.")
        for item in value:
            if "product_id" not in item or "quantity" not in item:
                raise serializers.ValidationError("Each product must have 'product_id' and 'quantity'.")
        return value
