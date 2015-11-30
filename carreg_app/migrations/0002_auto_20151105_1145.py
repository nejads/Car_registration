# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carreg_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='tag_id',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='tel',
            field=models.CharField(max_length=50),
        ),
    ]
