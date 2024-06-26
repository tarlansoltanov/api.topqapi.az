# Generated by Django 5.0 on 2024-05-20 09:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0001_initial'),
        ('supplier', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='catalog', to='product.product')),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='catalog', to='supplier.supplier')),
            ],
            options={
                'verbose_name': 'ProductRecord',
                'verbose_name_plural': 'ProductRecords',
                'ordering': ('-updated_at',),
                'abstract': False,
            },
        ),
    ]
