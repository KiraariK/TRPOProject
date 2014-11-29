# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dishes', '0004_auto_20141129_1924'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='composition',
            field=models.CharField(null=True, max_length=120, verbose_name='Состав', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='dish',
            name='description',
            field=models.CharField(null=True, max_length=250, verbose_name='Описание', blank=True),
            preserve_default=True,
        ),
    ]
