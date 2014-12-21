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
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=30, verbose_name='Название')),
                ('description', models.CharField(max_length=250, blank=True, null=True, verbose_name='Описание')),
                ('composition', models.CharField(max_length=120, blank=True, null=True, verbose_name='Состав')),
                ('dish_image', models.ImageField(upload_to='dishes/', blank=True, null=True, verbose_name='Картинка блюда')),
                ('weight', models.IntegerField(blank=True, null=True, verbose_name='Вес')),
                ('price', models.FloatField(default=100.0, verbose_name='Цена')),
                ('category', models.CharField(max_length=1, verbose_name='Категория блюда', choices=[('0', 'Алкогольные напитки'), ('1', 'Безалкогольные напитки'), ('2', 'Гарниры'), ('3', 'Горячие блюда'), ('4', 'Дессерты'), ('5', 'Закуски'), ('6', 'Салаты'), ('7', 'Пиццы'), ('8', 'Роллы'), ('9', 'Супы')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EstablishmentDish',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('dish', models.OneToOneField(to='dishes.Dish', verbose_name='Блюдо')),
                ('establishment', models.ForeignKey(to='establishments.Establishment', verbose_name='Заведение', related_name='dishes')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
