from rest_framework import serializers

from core.models import Contacts


class ContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = '__all__'


class ContactsCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = '__all__'


class ContactsUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = '__all__'


class ContactsDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = ['id']
