# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dishes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='category',
            field=models.CharField(max_length=1, verbose_name='Категория блюда', choices=[('0', 'Все категории'), ('1', 'Алкогольные напитки'), ('2', 'Безалкогольные напитки'), ('3', 'Супы'), ('4', 'Гарниры'), ('5', 'Горячие блюда'), ('6', 'Дессерты'), ('7', 'Закуски'), ('8', 'Салаты'), ('9', 'Пицы'), ('10', 'Роллы')]),
            preserve_default=True,
        ),
    ]
