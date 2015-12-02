# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Refuel',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('line', models.CharField(max_length=23)),
                ('consumption', models.PositiveIntegerField()),
                ('refuel_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('password', models.CharField(verbose_name='password', max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('tag_id', models.CharField(unique=True, max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(unique=True, max_length=254)),
                ('plate', models.CharField(max_length=30)),
                ('bank', models.CharField(max_length=30)),
                ('tel', models.CharField(max_length=50)),
                ('is_active', models.BooleanField(default=False)),
                ('is_admin', models.BooleanField(default=False)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='refuel',
            name='user',
            field=models.ForeignKey(related_name='refuels', to='carreg_app.User'),
        ),
    ]
