# Generated by Django 5.0 on 2024-02-28 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='type',
            field=models.PositiveSmallIntegerField(choices=[(0, 'İstifadəçi'), (1, 'Müdür'), (2, 'Anbar'), (3, 'Mağaza')], default=0),
        ),
    ]
