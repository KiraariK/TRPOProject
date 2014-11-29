# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('establishments', '0004_auto_20141129_2001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='establishment',
            name='establishment_image',
            field=models.ImageField(null=True, blank=True, upload_to='/establishment/', verbose_name='Логотип'),
            preserve_default=True,
        ),
    ]
