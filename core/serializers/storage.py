from rest_framework import serializers

from core.models import Storage, Contacts, Products, Factory
from core.serializers.contacts import ContactsSerializer
from core.serializers.factory import FactorySerializer
from core.serializers.products import ProductsSerializer


class StorageSerializer(serializers.ModelSerializer):
    provider = FactorySerializer(many=False, read_only=True)
    contacts = ContactsSerializer(many=False, read_only=True)
    products = ProductsSerializer(many=False, read_only=True)

    class Meta:
        model = Storage
        fields = '__all__'


class StorageCreateSerializer(serializers.ModelSerializer):
    provider = serializers.SlugRelatedField(
        required=False,
        many=False,
        queryset=Factory.objects.all(),
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
        model = Storage
        fields = '__all__'


class StorageUpdateSerializer(serializers.ModelSerializer):
    provider = serializers.SlugRelatedField(
        required=False,
        many=False,
        queryset=Factory.objects.all(),
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
        model = Storage
        fields = '__all__'


class StorageDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Storage
        fields = ['id']
