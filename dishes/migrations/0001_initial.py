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
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30, verbose_name='Название')),
                ('description', models.CharField(max_length=250, blank=True, null=True, verbose_name='Описание')),
                ('composition', models.CharField(max_length=120, blank=True, null=True, verbose_name='Состав')),
                ('dish_image', models.ImageField(upload_to='dishes/', blank=True, null=True, verbose_name='Картинка блюда')),
                ('weight', models.IntegerField(verbose_name='Вес', blank=True, null=True)),
                ('price', models.FloatField(verbose_name='Цена', default=100.0)),
                ('category', models.CharField(max_length=1, choices=[('0', 'Алкогольные напитки'), ('1', 'Безалкогольные напитки'), ('2', 'Гарниры'), ('3', 'Горячие блюда'), ('4', 'Дессерты'), ('5', 'Закуски'), ('6', 'Салаты'), ('7', 'Пицы'), ('8', 'Роллы'), ('9', 'Супы')], verbose_name='Категория блюда')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EstablishmentDish',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('dish', models.OneToOneField(related_name='+', to='dishes.Dish', verbose_name='Блюдо')),
                ('establishment', models.ForeignKey(related_name='dishes', to='establishments.Establishment', verbose_name='Заведение')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
