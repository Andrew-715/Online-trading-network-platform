from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView, CreateAPIView, \
    UpdateAPIView, RetrieveAPIView, DestroyAPIView

from core.models import Retail
from core.serializers.retail import RetailSerializer, \
    RetailCreateSerializer, RetailUpdateSerializer, RetailDeleteSerializer


class RetailListView(ListAPIView):
    queryset = Retail.objects.all()
    serializer_class = RetailSerializer
    filter_backends = [SearchFilter]
    search_fields = ['contacts__country']


class RetailRetrieveView(RetrieveAPIView):
    queryset = Retail.objects.all()
    serializer_class = RetailSerializer


class RetailCreateView(CreateAPIView):
    queryset = Retail.objects.all()
    serializer_class = RetailCreateSerializer


class RetailUpdateView(UpdateAPIView):
    queryset = Retail.objects.all()
    serializer_class = RetailUpdateSerializer


class RetailDestroyView(DestroyAPIView):
    queryset = Retail.objects.all()
    serializer_class = RetailDeleteSerializer
