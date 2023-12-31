from .models import Product
from .serializers import ProductSerializer
from rest_framework import viewsets, permissions

class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProductSerializer
