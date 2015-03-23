# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_article_create_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('status', models.CharField(max_length=1, choices=[(b'd', b'Draft'), (b'p', b'Published'), (b'w', b'Withdrawn')])),
                ('create_date', models.DateTimeField(verbose_name=b'date created')),
                ('modify_date', models.DateTimeField(verbose_name=b'date last modified')),
                ('priority', models.IntegerField()),
                ('cost', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('agegroup', models.CharField(max_length=100)),
                ('start_date', models.DateTimeField(verbose_name=b'start date')),
                ('end_date', models.DateTimeField(verbose_name=b'end date')),
                ('cost', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='Article',
        ),
    ]
