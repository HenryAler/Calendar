# Generated by Django 5.0.1 on 2024-02-27 15:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0005_remove_service_barber_barber_service'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='barber',
            name='service',
        ),
        migrations.AddField(
            model_name='barber',
            name='service',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='services.service'),
        ),
    ]
