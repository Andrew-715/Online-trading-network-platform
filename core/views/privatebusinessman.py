from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView, CreateAPIView, \
    UpdateAPIView, RetrieveAPIView, DestroyAPIView

from core.models import PrivateBusinessman
from core.serializers.privatebusinessman import PrivateBusinessmanSerializer, \
    PrivateBusinessmanCreateSerializer, PrivateBusinessmanUpdateSerializer, \
    PrivateBusinessmanDeleteSerializer


class PrivateBusinessmanListView(ListAPIView):
    queryset = PrivateBusinessman.objects.all()
    serializer_class = PrivateBusinessmanSerializer
    filter_backends = [SearchFilter]
    search_fields = ['contacts__country']


class PrivateBusinessmanRetrieveView(RetrieveAPIView):
    queryset = PrivateBusinessman.objects.all()
    serializer_class = PrivateBusinessmanSerializer


class PrivateBusinessmanCreateView(CreateAPIView):
    queryset = PrivateBusinessman.objects.all()
    serializer_class = PrivateBusinessmanCreateSerializer


class PrivateBusinessmanUpdateView(UpdateAPIView):
    queryset = PrivateBusinessman.objects.all()
    serializer_class = PrivateBusinessmanUpdateSerializer


class PrivateBusinessmanDestroyView(DestroyAPIView):
    queryset = PrivateBusinessman.objects.all()
    serializer_class = PrivateBusinessmanDeleteSerializer
