# Generated by Django 5.0.1 on 2024-03-02 14:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barber', '0004_delete_client_delete_record'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScheduleBarber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.DateField(null=True)),
                ('time', models.TimeField(null=True)),
                ('barber', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='barber.barber')),
            ],
        ),
    ]
