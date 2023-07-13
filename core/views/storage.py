from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView, CreateAPIView, \
    UpdateAPIView, RetrieveAPIView, DestroyAPIView

from core.models import Storage
from core.serializers.storage import StorageSerializer, \
    StorageCreateSerializer, StorageUpdateSerializer, StorageDeleteSerializer


class StorageListView(ListAPIView):
    queryset = Storage.objects.all()
    serializer_class = StorageSerializer
    filter_backends = [SearchFilter]
    search_fields = ['contacts__country']


class StorageRetrieveView(RetrieveAPIView):
    queryset = Storage.objects.all()
    serializer_class = StorageSerializer


class StorageCreateView(CreateAPIView):
    queryset = Storage.objects.all()
    serializer_class = StorageCreateSerializer


class StorageUpdateView(UpdateAPIView):
    queryset = Storage.objects.all()
    serializer_class = StorageUpdateSerializer


class StorageDestroyView(DestroyAPIView):
    queryset = Storage.objects.all()
    serializer_class = StorageDeleteSerializer
