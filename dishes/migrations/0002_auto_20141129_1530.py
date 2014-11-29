# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dishes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dish',
            name='dish_image',
            field=models.ImageField(blank=True, null=True, width_field=100, height_field=100, upload_to='', verbose_name='Картинка'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='dish',
            name='category',
            field=models.CharField(verbose_name='Категория блюда', choices=[('0', 'Алкогольные напитки'), ('1', 'Безалкогольные напитки'), ('2', 'Гарниры'), ('3', 'Горячие блюда'), ('4', 'Дессерты'), ('5', 'Закуски'), ('6', 'Салаты'), ('7', 'Пицы'), ('8', 'Роллы'), ('9', 'Супы')], max_length=1),
            preserve_default=True,
        ),
    ]
