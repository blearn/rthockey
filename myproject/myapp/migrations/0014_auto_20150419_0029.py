# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0013_auto_20150418_2356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 19, 0, 29, 13, 549939, tzinfo=utc), editable=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='customer',
            name='modify_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 19, 0, 29, 13, 549976, tzinfo=utc), editable=False),
            preserve_default=True,
        ),
    ]
