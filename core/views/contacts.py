from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView, CreateAPIView, \
    UpdateAPIView, RetrieveAPIView, DestroyAPIView

from core.models import Contacts
from core.serializers.contacts import ContactsSerializer, \
    ContactsCreateSerializer, ContactsUpdateSerializer, ContactsDeleteSerializer


class ContactsListView(ListAPIView):
    queryset = Contacts.objects.all()
    serializer_class = ContactsSerializer
    filter_backends = [SearchFilter]
    search_fields = ['country']


class ContactsRetrieveView(RetrieveAPIView):
    queryset = Contacts.objects.all()
    serializer_class = ContactsSerializer


class ContactsCreateView(CreateAPIView):
    queryset = Contacts.objects.all()
    serializer_class = ContactsCreateSerializer


class ContactsUpdateView(UpdateAPIView):
    queryset = Contacts.objects.all()
    serializer_class = ContactsUpdateSerializer


class ContactsDestroyView(DestroyAPIView):
    queryset = Contacts.objects.all()
    serializer_class = ContactsDeleteSerializer
