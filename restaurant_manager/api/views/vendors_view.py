from django.forms import model_to_dict
from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from restaurant_manager.api.decorators import use_transaction_atomic_and_handle_exceptions
from restaurant_manager.api.serializers import VendorSerializer, VendorContactSerializer
from restaurant_manager.models import Vendors


class VendorsView(viewsets.ViewSet):
    permission_classes = [AllowAny]

    @use_transaction_atomic_and_handle_exceptions
    def list(self, request):
        temp = {}
        for vendor in VendorSerializer(Vendors.objects.all(), many=True).data:
            temp[vendor['id']] = vendor
        return Response(data=temp, status=status.HTTP_200_OK)

    @use_transaction_atomic_and_handle_exceptions
    def retrieve(self, request, pk):
        return Response(data=VendorSerializer(Vendors.objects.get(id=pk)).data, status=status.HTTP_200_OK)

    @use_transaction_atomic_and_handle_exceptions
    def create(self, request):
        vendor_serializer = VendorSerializer(data=request.data)
        vendor_serializer.is_valid(raise_exception=True)
        created_vendor = vendor_serializer.save()

        for contact in request.data['contacts']:
            vendor_contact_serializer = VendorContactSerializer(data=contact)
            vendor_contact_serializer.is_valid(raise_exception=True)
            vendor_contact_serializer.save(vendor=created_vendor)

        return Response(data=model_to_dict(created_vendor, fields=['id']), status=status.HTTP_201_CREATED)

    @use_transaction_atomic_and_handle_exceptions
    def update(self, request, pk):
        serializer = VendorSerializer(Vendors.objects.get(id=pk), data=request.data)
        serializer.is_valid(raise_exception=True)
        updated = serializer.save()

        return Response(status=status.HTTP_200_OK)
