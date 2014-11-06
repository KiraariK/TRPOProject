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
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=20)),
                ('description', models.CharField(null=True, max_length=100, blank=True)),
                ('composition', models.CharField(null=True, max_length=50, blank=True)),
                ('weight', models.IntegerField(null=True, blank=True)),
                ('price', models.FloatField()),
                ('category', models.CharField(max_length=1, choices=[('0', 'alcohol'), ('1', 'soft_drinks'), ('2', 'garnishes'), ('3', 'hot_dishes'), ('4', 'desserts'), ('5', 'snakes'), ('6', 'salads'), ('7', 'pizzas'), ('8', 'rolls')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
