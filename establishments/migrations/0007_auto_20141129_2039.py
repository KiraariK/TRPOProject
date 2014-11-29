# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('establishments', '0006_auto_20141129_2013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='establishment',
            name='establishment_image',
            field=models.ImageField(null=True, verbose_name='Логотип', blank=True, upload_to='establishments/'),
            preserve_default=True,
        ),
    ]
