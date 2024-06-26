# Generated by Django 5.0 on 2024-05-20 09:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255, unique=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='category.category')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
                'ordering': ('-updated_at',),
                'abstract': False,
            },
        ),
    ]
