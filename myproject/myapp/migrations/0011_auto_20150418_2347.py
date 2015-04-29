# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_auto_20150414_0606'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=60, null=True, blank=True)),
                ('description', models.TextField(null=True, blank=True)),
                ('image', models.ImageField(upload_to=b'images/')),
                ('thumbnail1', models.ImageField(null=True, upload_to=b'images/', blank=True)),
                ('thumbnail2', models.ImageField(null=True, upload_to=b'images/', blank=True)),
                ('width', models.IntegerField(null=True, blank=True)),
                ('height', models.IntegerField(null=True, blank=True)),
                ('hidden', models.BooleanField()),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['created'],
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='customer',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 18, 23, 47, 35, 897640, tzinfo=utc), editable=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='customer',
            name='modify_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 18, 23, 47, 35, 897693, tzinfo=utc), editable=False),
            preserve_default=True,
        ),
    ]
