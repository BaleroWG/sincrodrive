# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-22 10:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProcesoActividad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('rutaorigen', models.CharField(max_length=255)),
                ('rutadestino', models.CharField(max_length=255)),
                ('extensiones', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ProcesoCopia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
    ]