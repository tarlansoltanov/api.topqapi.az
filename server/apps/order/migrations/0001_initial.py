# Generated by Django 5.0 on 2024-03-17 20:19

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('branch', '0001_initial'),
        ('product', '0001_initial'),
        ('staff', '0001_initial'),
        ('supplier', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('customer', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('note', models.TextField(blank=True)),
                ('discount', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('payed', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('seller_share', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('sale_date', models.DateField()),
                ('delivery_date', models.DateField(blank=True, null=True)),
                ('install_date', models.DateField(blank=True, null=True)),
                ('status', models.PositiveSmallIntegerField(choices=[(0, 'DRAFT'), (1, 'Sifariş qeydə olundu'), (2, 'Sifarişi Anbar qəbul etdi'), (3, 'Sifariş hazırlanır')], default=0)),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='branch.branch')),
                ('driver', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='staff.driver')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='staff.seller')),
                ('worker', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='staff.worker')),
            ],
            options={
                'verbose_name': 'Order',
                'verbose_name_plural': 'Orders',
                'ordering': ('-updated_at',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OrderCartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_cart', to='product.product')),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_cart', to='supplier.supplier')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_cart', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Order Cart Item',
                'verbose_name_plural': 'Order Cart Items',
                'ordering': ('-updated_at',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('quantity', models.PositiveSmallIntegerField(default=0)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='order.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_products', to='product.product')),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_products', to='supplier.supplier')),
            ],
            options={
                'verbose_name': 'Order Item',
                'verbose_name_plural': 'Order Items',
                'ordering': ('-updated_at',),
                'abstract': False,
            },
        ),
    ]
