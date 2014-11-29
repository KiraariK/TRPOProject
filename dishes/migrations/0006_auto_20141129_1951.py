# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dishes', '0005_auto_20141129_1926'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='dish_image',
            field=models.ImageField(verbose_name='Картинка блюда', blank=True, upload_to='dishes/', null=True),
            preserve_default=True,
        ),
    ]
