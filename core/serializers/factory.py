from rest_framework import serializers

from core.models import Factory, Contacts, Products
from core.serializers.contacts import ContactsSerializer
from core.serializers.products import ProductsSerializer


class FactorySerializer(serializers.ModelSerializer):
    contacts = ContactsSerializer(many=False, read_only=True)
    products = ProductsSerializer(many=False, read_only=True)

    class Meta:
        model = Factory
        fields = '__all__'


class FactoryCreateSerializer(serializers.ModelSerializer):
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
        model = Factory
        fields = '__all__'


class FactoryUpdateSerializer(serializers.ModelSerializer):
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
        model = Factory
        fields = '__all__'


class FactoryDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Factory
        fields = ['id']
