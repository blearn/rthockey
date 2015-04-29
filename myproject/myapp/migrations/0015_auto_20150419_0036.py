# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0014_auto_20150419_0029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 19, 0, 36, 26, 45191, tzinfo=utc), editable=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='customer',
            name='modify_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 19, 0, 36, 26, 45226, tzinfo=utc), editable=False),
            preserve_default=True,
        ),
    ]
