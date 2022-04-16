from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from restaurant_manager.api.decorators import use_transaction_atomic_and_handle_exceptions
from restaurant_manager.api.serializers import VendorSerializer
from restaurant_manager.models import Vendors


class VendorsView(viewsets.ViewSet):
    permission_classes = [AllowAny]

    @use_transaction_atomic_and_handle_exceptions
    def list(self, request):
        return Response(data=VendorSerializer(Vendors.objects.all(), many=True).data, status=status.HTTP_200_OK)
