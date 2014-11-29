# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('establishments', '0002_establishment_establishment_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='establishment',
            name='establishment_image',
            field=models.ImageField(verbose_name='Логотип', blank=True, upload_to='establishment/', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='establishmentbranch',
            name='address',
            field=models.CharField(verbose_name='Адресс', max_length=80),
            preserve_default=True,
        ),
    ]
