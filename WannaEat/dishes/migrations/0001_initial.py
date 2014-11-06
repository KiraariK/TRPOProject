# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=100, blank=True)),
                ('composition', models.CharField(max_length=50, blank=True)),
                ('weight', models.IntegerField(blank=True)),
                ('price', models.FloatField()),
                ('category', models.CharField(choices=[('0', 'alcohol'), ('1', 'soft_drinks'), ('2', 'garnishes'), ('3', 'hot_dishes'), ('4', 'desserts'), ('5', 'snaks'), ('6', 'salads'), ('7', 'pizzas'), ('8', 'rolls')], max_length=1)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EstablishmentDishes',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('dish', models.ForeignKey(to='dishes.Dish')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
