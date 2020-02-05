from rest_framework import serializers
from .models import Product, LANGUAGE_CHOICES, STYLE_CHOICES


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'price', 'stock', 'description', 'pub_date', 'last_date', 'author', 'image', 'slug']