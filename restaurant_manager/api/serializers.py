from rest_framework import serializers

from restaurant_manager.models import Vendors, VendorContacts


class VendorContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = VendorContacts
        fields = '__all__'


class VendorSerializer(serializers.ModelSerializer):
    contacts = VendorContactSerializer(many=True)

    class Meta:
        model = Vendors
        fields = '__all__'
