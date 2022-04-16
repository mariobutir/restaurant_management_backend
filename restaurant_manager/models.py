from django.db import models


class Vendors(models.Model):
    name = models.CharField(max_length=100, unique=True)
    address = models.CharField(max_length=100)
    gst = models.FloatField()
    lead_time = models.FloatField()
    payment_terms = models.CharField(max_length=1000)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'vendors'


class VendorContacts(models.Model):
    vendor = models.ForeignKey(Vendors, on_delete=models.CASCADE, related_name='contacts')
    name = models.CharField(max_length=100)
    number = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'vendor_contacts'
        unique_together = ['vendor', 'email']
