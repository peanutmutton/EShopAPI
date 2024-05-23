from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.Serializer):
    class Meta:
        model = Product
        fields = ['name', 'description']
    name = serializers.CharField(required=True, max_length=30)
    description = serializers.CharField(style={'base_template': 'textarea.html'})

    def create(self, validated_data):
        return Product.objects.create(**validated_data)