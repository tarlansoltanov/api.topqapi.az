# Generated by Django 5.0 on 2024-03-08 13:37

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
        ('warehouse', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='warehouse_cart', to='product.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='warehouse_cart', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Cart Item',
                'verbose_name_plural': 'Cart Items',
                'ordering': ('-updated_at',),
                'abstract': False,
            },
        ),
    ]