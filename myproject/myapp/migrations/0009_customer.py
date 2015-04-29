# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_auto_20150312_0104'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('birthdate', models.DateField()),
                ('address', models.CharField(max_length=1000)),
                ('parent_guardian_name', models.CharField(max_length=200)),
                ('home_phone', models.CharField(max_length=15)),
                ('email', models.CharField(max_length=250)),
                ('emergency_contact', models.CharField(max_length=1000)),
                ('medical_conditions', models.CharField(max_length=65535)),
                ('height_inches', models.CharField(max_length=2)),
                ('weight_pounds', models.CharField(max_length=3)),
                ('is_locked', models.BooleanField(default=True)),
                ('other_phones', models.CharField(max_length=1000)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
