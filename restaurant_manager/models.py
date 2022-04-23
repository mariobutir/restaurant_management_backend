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


class ProductCategories(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'product_categories'


class ProductUnitTypes(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'product_unit_types'


class Products(models.Model):
    vendors = models.ManyToManyField(Vendors, related_name='products', through='ProductVendors', through_fields=('product', 'vendor'))
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    category = models.ForeignKey(ProductCategories, on_delete=models.RESTRICT, related_name='products')
    unit = models.ForeignKey(ProductUnitTypes, on_delete=models.RESTRICT, related_name='products')
    shelf_life = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'products'


class ProductVendors(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    vendor = models.ForeignKey(Vendors, on_delete=models.CASCADE)

    class Meta:
        db_table = 'product_vendors'
