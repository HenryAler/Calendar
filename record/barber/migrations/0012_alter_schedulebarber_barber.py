# Generated by Django 5.0.1 on 2024-03-02 14:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barber', '0011_remove_schedulebarber_durations'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedulebarber',
            name='barber',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='barber.barber', verbose_name='Мастер'),
        ),
    ]
