# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dishes', '0002_auto_20141130_2142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='category',
            field=models.CharField(choices=[('0', 'Алкогольные напитки'), ('1', 'Безалкогольные напитки'), ('2', 'Гарниры'), ('3', 'Горячие блюда'), ('4', 'Дессерты'), ('5', 'Закуски'), ('6', 'Салаты'), ('7', 'Пицы'), ('8', 'Роллы')], max_length=1, verbose_name='Категория блюда'),
            preserve_default=True,
        ),
    ]
