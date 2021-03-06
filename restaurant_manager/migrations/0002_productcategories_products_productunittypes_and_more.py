# Generated by Django 4.0.4 on 2022-04-23 10:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant_manager', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductCategories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'product_categories',
            },
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('brand', models.CharField(max_length=100)),
                ('shelf_life', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='products', to='restaurant_manager.productcategories')),
            ],
            options={
                'db_table': 'products',
            },
        ),
        migrations.CreateModel(
            name='ProductUnitTypes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'product_unit_types',
            },
        ),
        migrations.CreateModel(
            name='ProductVendors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant_manager.products')),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant_manager.vendors')),
            ],
            options={
                'db_table': 'product_vendors',
            },
        ),
        migrations.AddField(
            model_name='products',
            name='unit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='products', to='restaurant_manager.productunittypes'),
        ),
        migrations.AddField(
            model_name='products',
            name='vendors',
            field=models.ManyToManyField(related_name='products', through='restaurant_manager.ProductVendors', to='restaurant_manager.vendors'),
        ),
    ]
