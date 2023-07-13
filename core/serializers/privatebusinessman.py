from rest_framework import serializers

from core.models import PrivateBusinessman, Storage, Contacts, Products
from core.serializers.contacts import ContactsSerializer
from core.serializers.products import ProductsSerializer
from core.serializers.storage import StorageSerializer


class PrivateBusinessmanSerializer(serializers.ModelSerializer):
    provider = StorageSerializer(many=False, read_only=True)
    contacts = ContactsSerializer(many=False, read_only=True)
    products = ProductsSerializer(many=False, read_only=True)

    class Meta:
        model = PrivateBusinessman
        fields = '__all__'


class PrivateBusinessmanCreateSerializer(serializers.ModelSerializer):
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
        model = PrivateBusinessman
        fields = '__all__'


class PrivateBusinessmanUpdateSerializer(serializers.ModelSerializer):
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
        model = PrivateBusinessman
        fields = '__all__'


class PrivateBusinessmanDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrivateBusinessman
        fields = ['id']
