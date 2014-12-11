# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dishes', '0003_auto_20141130_2226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='establishmentdish',
            name='dish',
            field=models.OneToOneField(verbose_name='Блюдо', to='dishes.Dish'),
            preserve_default=True,
        ),
    ]
