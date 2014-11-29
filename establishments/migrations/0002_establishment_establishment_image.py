# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('establishments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='establishment',
            name='establishment_image',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Логотип'),
            preserve_default=True,
        ),
    ]
