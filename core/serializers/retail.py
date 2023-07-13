from rest_framework import serializers

from core.models import Retail, Storage, Contacts, Products
from core.serializers.contacts import ContactsSerializer
from core.serializers.products import ProductsSerializer
from core.serializers.storage import StorageSerializer


class RetailSerializer(serializers.ModelSerializer):
    provider = StorageSerializer(many=False, read_only=True)
    contacts = ContactsSerializer(many=False, read_only=True)
    products = ProductsSerializer(many=False, read_only=True)

    class Meta:
        model = Retail
        fields = '__all__'


class RetailCreateSerializer(serializers.ModelSerializer):
    provider = serializers.SlugRelatedField(
        required=False,
        many=False,
        queryset=Storage.objects.all(),
        slug_field='name'
    )
    contacts = serializers.SlugRelatedField(
        required=False,
        many=False,
        queryset=Contacts.objects.all(),
        slug_field='email'
    )
    products = serializers.SlugRelatedField(
        required=False,
        many=False,
        queryset=Products.objects.all(),
        slug_field='name'
    )

    class Meta:
        model = Retail
        fields = '__all__'


class RetailUpdateSerializer(serializers.ModelSerializer):
    provider = serializers.SlugRelatedField(
        required=False,
        many=False,
        queryset=Storage.objects.all(),
        slug_field='name'
    )
    contacts = serializers.SlugRelatedField(
        required=False,
        many=False,
        queryset=Contacts.objects.all(),
        slug_field='email'
    )
    products = serializers.SlugRelatedField(
        required=False,
        many=False,
        queryset=Products.objects.all(),
        slug_field='name'
    )
    arrears_over_provider = serializers.FloatField(
        read_only=True)

    class Meta:
        model = Retail
        fields = '__all__'


class RetailDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Retail
        fields = ['id']
