from django.urls import include, path
from rest_framework import routers

from restaurant_manager.api.views.vendors_view import VendorsView

router = routers.DefaultRouter()
router.register(r'vendors', VendorsView, basename='vendors')

urlpatterns = [
    path('', include(router.urls)),
]
