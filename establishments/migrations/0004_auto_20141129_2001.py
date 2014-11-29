# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('establishments', '0003_auto_20141129_1951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='establishment',
            name='establishment_image',
            field=models.ImageField(verbose_name='Логотип', upload_to='/static/images/establishment/', blank=True, null=True),
            preserve_default=True,
        ),
    ]
