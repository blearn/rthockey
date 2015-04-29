# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0012_auto_20150418_2348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 18, 23, 56, 39, 711839, tzinfo=utc), editable=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='customer',
            name='modify_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 18, 23, 56, 39, 711873, tzinfo=utc), editable=False),
            preserve_default=True,
        ),
    ]
