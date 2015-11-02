# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import carreg_app.utils


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Credential',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('encrypted_pass', models.CharField(max_length=128)),
                ('salt', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Refuel',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('line', models.CharField(max_length=23)),
                ('consumption', models.PositiveIntegerField()),
                ('refuel_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('tag_id', models.CharField(max_length=23, unique=True)),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('plate', models.CharField(max_length=30)),
                ('bank', models.CharField(max_length=30)),
                ('tel', models.CharField(validators=[carreg_app.utils.validate_phone], max_length=23)),
                ('registration_time', models.DateTimeField(auto_now_add=True)),
                ('latest_modification', models.DateTimeField(auto_now=True)),
                ('credential', models.OneToOneField(to='carreg_app.Credential')),
            ],
        ),
        migrations.AddField(
            model_name='refuel',
            name='user',
            field=models.ForeignKey(to='carreg_app.User', related_name='refuels'),
        ),
    ]
