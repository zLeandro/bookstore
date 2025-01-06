from rest_framework.authentication import (
    TokenAuthentication,
)

from rest_framework.viewsets import ModelViewSet
from product.models.product import Product
from product.serializers.product_serializer import ProductSerializer


class ProductViewSet(ModelViewSet):
    authentication_classes = [TokenAuthentication]
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.all().order_by("id")
