# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dishes', '0006_auto_20141129_1951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='dish_image',
            field=models.ImageField(verbose_name='Картинка блюда', upload_to='/static/images/dishes/', blank=True, null=True),
            preserve_default=True,
        ),
    ]
