# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_auto_20150309_0353'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=500)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='program',
            name='location',
            field=models.ForeignKey(default=1, to='myapp.Location'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='session',
            name='location',
            field=models.ForeignKey(default=1, to='myapp.Location'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='session',
            name='program',
            field=models.ForeignKey(default=1, to='myapp.Program'),
            preserve_default=False,
        ),
    ]
