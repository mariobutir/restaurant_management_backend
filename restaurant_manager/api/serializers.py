from rest_framework import serializers

from restaurant_manager.models import Vendors, VendorContacts


class VendorContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = VendorContacts
        fields = ['name', 'number', 'email']


class VendorSerializer(serializers.ModelSerializer):
    contacts = VendorContactSerializer(many=True, read_only=True)

    class Meta:
        model = Vendors
        fields = '__all__'
