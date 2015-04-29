# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 14, 6, 6, 44, 735116, tzinfo=utc), editable=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='customer',
            name='modify_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 14, 6, 6, 44, 735164, tzinfo=utc), editable=False),
            preserve_default=True,
        ),
    ]
