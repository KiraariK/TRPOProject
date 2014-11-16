# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('establishments', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(verbose_name='Название', max_length=30)),
                ('description', models.CharField(null=True, blank=True, verbose_name='Описание', max_length=100)),
                ('composition', models.CharField(null=True, blank=True, verbose_name='Состав', max_length=50)),
                ('weight', models.IntegerField(null=True, blank=True, verbose_name='Вес')),
                ('price', models.FloatField(default=100.0, verbose_name='Цена')),
                ('category', models.CharField(choices=[('0', 'Алкогольные напитки'), ('1', 'Безалкогольные напитки'), ('2', 'Гарниры'), ('3', 'Горячие блюда'), ('4', 'Дессерты'), ('5', 'Закуски'), ('6', 'Салаты'), ('7', 'Пицы'), ('8', 'Роллы')], verbose_name='Категория блюда', max_length=1)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EstablishmentDish',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('dish', models.OneToOneField(to='dishes.Dish', verbose_name='Блюдо', related_name='+')),
                ('establishment', models.ForeignKey(to='establishments.Establishment', verbose_name='Заведение', related_name='dishes')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
