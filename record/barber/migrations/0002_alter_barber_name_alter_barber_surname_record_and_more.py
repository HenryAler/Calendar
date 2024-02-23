# Generated by Django 5.0.1 on 2024-02-03 20:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barber', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='barber',
            name='name',
            field=models.CharField(max_length=15, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='barber',
            name='surname',
            field=models.CharField(max_length=15, verbose_name='Фамилия'),
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('surname', models.CharField(max_length=15)),
                ('fone', models.IntegerField()),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('barber', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='barber.barber')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.DeleteModel(
            name='Records',
        ),
    ]
