from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView, CreateAPIView, \
    UpdateAPIView, RetrieveAPIView, DestroyAPIView

from core.models import Factory
from core.serializers.factory import FactorySerializer, \
    FactoryCreateSerializer, FactoryUpdateSerializer, FactoryDeleteSerializer


class FactoryListView(ListAPIView):
    queryset = Factory.objects.all()
    serializer_class = FactorySerializer
    filter_backends = [SearchFilter]
    search_fields = ['contacts__country']


class FactoryRetrieveView(RetrieveAPIView):
    queryset = Factory.objects.all()
    serializer_class = FactorySerializer


class FactoryCreateView(CreateAPIView):
    queryset = Factory.objects.all()
    serializer_class = FactoryCreateSerializer


class FactoryUpdateView(UpdateAPIView):
    queryset = Factory.objects.all()
    serializer_class = FactoryUpdateSerializer


class FactoryDestroyView(DestroyAPIView):
    queryset = Factory.objects.all()
    serializer_class = FactoryDeleteSerializer
