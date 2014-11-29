# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dishes', '0007_auto_20141129_2001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='dish_image',
            field=models.ImageField(null=True, blank=True, upload_to='/dishes/', verbose_name='Картинка блюда'),
            preserve_default=True,
        ),
    ]
