# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dishes', '0002_auto_20141129_1530'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='dish_image',
            field=models.ImageField(upload_to='', width_field=300, height_field=300, null=True, blank=True, verbose_name='Картинка'),
            preserve_default=True,
        ),
    ]
