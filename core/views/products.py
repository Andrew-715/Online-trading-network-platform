from rest_framework.generics import ListAPIView, CreateAPIView, \
    UpdateAPIView, RetrieveAPIView, DestroyAPIView

from core.models import Products
from core.serializers.products import ProductsSerializer, \
    ProductsCreateSerializer, ProductsUpdateSerializer, ProductsDeleteSerializer


class ProductsListView(ListAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer


class ProductsRetrieveView(RetrieveAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer


class ProductsCreateView(CreateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsCreateSerializer


class ProductsUpdateView(UpdateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsUpdateSerializer


class ProductsDestroyView(DestroyAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsDeleteSerializer
