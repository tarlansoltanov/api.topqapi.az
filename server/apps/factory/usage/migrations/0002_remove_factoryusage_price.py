# Generated by Django 5.0 on 2024-03-23 11:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('factory_usage', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='factoryusage',
            name='price',
        ),
    ]