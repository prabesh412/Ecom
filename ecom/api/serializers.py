from ecom.models import product
from rest_framework import serializers


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = product
        fields = ['id', 'product_name', 'product_image', 'price']