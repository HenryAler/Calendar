# Generated by Django 5.0.1 on 2024-03-14 10:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barber', '0016_alter_price_barber_alter_price_durations_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schedulebarber',
            name='barber',
        ),
        migrations.AddField(
            model_name='schedulebarber',
            name='barber',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='barber.barber', verbose_name='Мастер'),
        ),
    ]
