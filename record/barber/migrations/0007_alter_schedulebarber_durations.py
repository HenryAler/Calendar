# Generated by Django 5.0.1 on 2024-03-02 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barber', '0006_remove_schedulebarber_time_schedulebarber_durations'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedulebarber',
            name='durations',
            field=models.DurationField(default=720, null=True),
        ),
    ]
