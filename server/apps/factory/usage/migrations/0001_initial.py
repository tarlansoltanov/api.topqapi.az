# Generated by Django 5.0 on 2024-03-23 10:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('factory_product', '0001_initial'),
        ('factory_storage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FactoryUsage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('quantity', models.PositiveSmallIntegerField(default=0)),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('date', models.DateField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usages', to='factory_product.factoryproduct')),
            ],
            options={
                'verbose_name': 'Factory Usagem',
                'verbose_name_plural': 'Factory Usagems',
                'ordering': ('-updated_at',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FactoryUsageItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('quantity', models.PositiveIntegerField()),
                ('storage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usages', to='factory_storage.factorystorageitem')),
                ('usage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='factory_usage.factoryusage')),
            ],
            options={
                'verbose_name': 'FactoryUsageItem',
                'verbose_name_plural': 'FactoryUsageItems',
                'ordering': ('-updated_at',),
                'abstract': False,
            },
        ),
    ]