# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_auto_20150311_0058'),
    ]

    operations = [
        migrations.AddField(
            model_name='session',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 11, 3, 12, 20, 482058, tzinfo=utc), editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='session',
            name='modify_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 11, 3, 12, 47, 889959, tzinfo=utc), editable=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='program',
            name='create_date',
            field=models.DateTimeField(editable=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='program',
            name='modify_date',
            field=models.DateTimeField(editable=False),
            preserve_default=True,
        ),
    ]
