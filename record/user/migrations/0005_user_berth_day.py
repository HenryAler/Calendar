# Generated by Django 5.0.1 on 2024-02-28 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_remove_user_berth_day'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='berth_day',
            field=models.DateField(null=True),
        ),
    ]
