# Generated by Django 5.0 on 2024-02-28 18:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('branch', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='branch',
            options={'ordering': ('-updated_at',), 'verbose_name': 'Branch', 'verbose_name_plural': 'Branches'},
        ),
    ]