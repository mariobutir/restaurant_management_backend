from rest_framework import serializers

from restaurant_manager.models import Vendors, VendorContacts, Products


class VendorContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = VendorContacts
        fields = ['id', 'name', 'number', 'email']


class VendorSerializer(serializers.ModelSerializer):
    contacts = VendorContactSerializer(many=True, read_only=True)

    class Meta:
        model = Vendors
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    vendors = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    category = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    unit = serializers.PrimaryKeyRelatedField(many=False, read_only=True)

    class Meta:
        model = Products
        fields = '__all__'
