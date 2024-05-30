# Generated by Django 5.0 on 2024-05-30 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='type',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Super Admin'), (1, 'Müdür'), (2, 'Anbar'), (3, 'Mağaza')], default=3),
        ),
    ]
