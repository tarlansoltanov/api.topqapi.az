# Generated by Django 5.1 on 2024-09-30 17:00

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
        ('warehouse', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('customer', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('note', models.TextField(blank=True)),
                ('payed', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('sale_date', models.DateField()),
                ('seller_share', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('delivery_price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('delivery_date', models.DateField(blank=True, null=True)),
                ('install_price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('install_date', models.DateField(blank=True, null=True)),
                ('status', models.PositiveSmallIntegerField(choices=[(0, 'DRAFT'), (1, 'Satış qeydə alındı'), (2, 'Anbar satışı qəbul etdi'), (3, 'Məhsullar hazırlanır'), (4, 'Məhsullar hazırdır'), (5, 'Geri Qayıtma'), (6, 'Məhsullar yoldadır'), (7, 'Məhsullar çatdırıldı'), (8, 'Satış tamamlandı')], default=0)),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='branch.branch')),
                ('driver', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='staff.driver')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='staff.seller')),
                ('worker', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='staff.worker')),
            ],
            options={
                'verbose_name': 'Order',
                'verbose_name_plural': 'Orders',
                'ordering': ('-updated_at',),
            },
        ),
        migrations.CreateModel(
            name='OrderCartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('quantity', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('size', models.CharField(blank=True, max_length=255)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_cart', to='product.product')),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_cart', to='supplier.supplier')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_cart', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Order Cart Item',
                'verbose_name_plural': 'Order Cart Items',
                'ordering': ('-updated_at',),
            },
        ),
        migrations.CreateModel(
            name='OrderExpense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='expenses', to='order.order')),
            ],
            options={
                'verbose_name': 'Order Expense',
                'verbose_name_plural': 'Order Expenses',
                'ordering': ('-updated_at',),
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('quantity', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('size', models.CharField(blank=True, max_length=255)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='order.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_products', to='product.product')),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_products', to='supplier.supplier')),
            ],
            options={
                'verbose_name': 'Order Item',
                'verbose_name_plural': 'Order Items',
                'ordering': ('-updated_at',),
            },
        ),
        migrations.CreateModel(
            name='OrderItemSale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('quantity', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('order_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sales', to='order.orderitem')),
                ('warehouse_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sales', to='warehouse.warehouseitem')),
            ],
            options={
                'verbose_name': 'Order Item Sale',
                'verbose_name_plural': 'Order Item Sales',
                'ordering': ('-updated_at',),
            },
        ),
    ]
