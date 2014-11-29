# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('establishments', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('establishment', models.OneToOneField(related_name='account', to='establishments.Establishment', verbose_name='Заведение')),
                ('user', models.ForeignKey(related_name='establishments_accounts', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
