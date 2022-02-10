from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ProductSerializer
from ecom.models import product
# Create your views here.

class ProductViewSet(viewsets.ModelViewSet):

    queryset = product.objects.all().order_by('id')
    serializer_class = ProductSerializer


