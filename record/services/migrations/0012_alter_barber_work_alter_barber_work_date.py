# Generated by Django 5.0.1 on 2024-02-28 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0011_alter_barber_work_alter_barber_work_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='barber',
            name='work',
            field=models.BooleanField(blank=True),
        ),
        migrations.AlterField(
            model_name='barber',
            name='work_date',
            field=models.DateField(blank=True),
        ),
    ]
